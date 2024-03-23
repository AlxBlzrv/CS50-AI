import pygame
import sys
import time

from Minesweeper_Game import GameMinesweeper, AIForMinesweeper

HEIGHT = 8
WIDTH = 8
MINES = 8

BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
WHITE = (255, 255, 255)

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)

OPEN_SANS = "D:/work/git/cs50-ai/Minesweeper/OpenSans-Regular.ttf"
small_font = pygame.font.Font(OPEN_SANS, 20)
medium_font = pygame.font.Font(OPEN_SANS, 28)
large_font = pygame.font.Font(OPEN_SANS, 40)

BOARD_PADDING = 20
board_width = ((2 / 3) * width) - (BOARD_PADDING * 2)
board_height = height - (BOARD_PADDING * 2)
cell_size = int(min(board_width / WIDTH, board_height / HEIGHT))
board_origin = (BOARD_PADDING, BOARD_PADDING)

flag = pygame.image.load("D:/work/git/cs50-ai/Minesweeper/flag.png")
flag = pygame.transform.scale(flag, (cell_size, cell_size))
mine = pygame.image.load("D:/work/git/cs50-ai/Minesweeper/mine.png")
mine = pygame.transform.scale(mine, (cell_size, cell_size))

game = GameMinesweeper(height=HEIGHT, width=WIDTH, mines=MINES)
ai = AIForMinesweeper(height=HEIGHT, width=WIDTH)

revealed = set()
flags = set()
lost = False

instructions = True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)

    if instructions:

        title = large_font.render("Play Minesweeper", True, WHITE)
        title_rect = title.get_rect()
        title_rect.center = ((width / 2), 50)
        screen.blit(title, title_rect)

        rules = [
            "Click a cell to reveal it.",
            "Right-click a cell to mark it as a mine.",
            "Mark all mines successfully to win!"
        ]
        for i, rule in enumerate(rules):
            line = small_font.render(rule, True, WHITE)
            line_rect = line.get_rect()
            line_rect.center = ((width / 2), 150 + 30 * i)
            screen.blit(line, line_rect)

        button_rect = pygame.Rect((width / 4), (3 / 4) * height, width / 2, 50)
        button_text = medium_font.render("Play Game", True, BLACK)
        button_text_rect = button_text.get_rect()
        button_text_rect.center = button_rect.center
        pygame.draw.rect(screen, WHITE, button_rect)
        screen.blit(button_text, button_text_rect)

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse):
                instructions = False
                time.sleep(0.3)

        pygame.display.flip()
        continue

    cells = []
    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):

            rect = pygame.Rect(
                board_origin[0] + j * cell_size,
                board_origin[1] + i * cell_size,
                cell_size, cell_size
            )
            pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, WHITE, rect, 3)

            if game.is_mine((i, j)) and lost:
                screen.blit(mine, rect)
            elif (i, j) in flags:
                screen.blit(flag, rect)
            elif (i, j) in revealed:
                neighbors = small_font.render(
                    str(game.nearby_mines((i, j))),
                    True, BLACK
                )
                neighbors_text_rect = neighbors.get_rect()
                neighbors_text_rect.center = rect.center
                screen.blit(neighbors, neighbors_text_rect)

            row.append(rect)
        cells.append(row)

    ai_button = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, (1 / 3) * height - 50,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    button_text = medium_font.render("AI Move", True, BLACK)
    button_rect = button_text.get_rect()
    button_rect.center = ai_button.center
    pygame.draw.rect(screen, WHITE, ai_button)
    screen.blit(button_text, button_rect)

    reset_button = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, (1 / 3) * height + 20,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    button_text = medium_font.render("Reset", True, BLACK)
    button_rect = button_text.get_rect()
    button_rect.center = reset_button.center
    pygame.draw.rect(screen, WHITE, reset_button)
    screen.blit(button_text, button_rect)

    text = "Lost" if lost else "Won" if game.mines == flags else ""
    text = medium_font.render(text, True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = ((5 / 6) * width, (2 / 3) * height)
    screen.blit(text, text_rect)

    move = None

    left, _, right = pygame.mouse.get_pressed()

    if right == 1 and not lost:
        mouse = pygame.mouse.get_pos()
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if cells[i][j].collidepoint(mouse) and (i, j) not in revealed:
                    if (i, j) in flags:
                        flags.remove((i, j))
                    else:
                        flags.add((i, j))
                    time.sleep(0.2)

    elif left == 1:
        mouse = pygame.mouse.get_pos()

        if ai_button.collidepoint(mouse) and not lost:
            move = ai.make_safe_move()
            if move is None:
                move = ai.make_random_move()
                if move is None:
                    flags = ai.mines.copy()
                    print("No moves left to make.")
                else:
                    print("No known safe moves, AI making random move.")
            else:
                print("AI making safe move.")
            time.sleep(0.2)

        elif reset_button.collidepoint(mouse):
            game = GameMinesweeper(height=HEIGHT, width=WIDTH, mines=MINES)
            ai = AIForMinesweeper(height=HEIGHT, width=WIDTH)
            revealed = set()
            flags = set()
            lost = False
            continue

        elif not lost:
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    if (cells[i][j].collidepoint(mouse)
                            and (i, j) not in flags
                            and (i, j) not in revealed):
                        move = (i, j)

    if move:
        if game.is_mine(move):
            lost = True
        else:
            nearby = game.nearby_mines(move)
            revealed.add(move)
            ai.add_knowledge(move, nearby)

    pygame.display.flip()