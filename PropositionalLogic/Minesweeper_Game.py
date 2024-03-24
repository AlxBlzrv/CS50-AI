import random
import copy


class GameMinesweeper():

    def __init__(self, height=8, width=8, mines=8):

        self.height = height
        self.width = width
        self.mines = set()

        self.field = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.field.append(row)

        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.field[i][j]:
                self.mines.add((i, j))
                self.field[i][j] = True

        self.mines_found = set()

    def display(self):
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.field[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.field[i][j]

    def nearby_mines(self, cell):

        count = 0

        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                if (i, j) == cell:
                    continue

                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.field[i][j]:
                        count += 1

        return count

    def game_won(self):
        return self.mines_found == self.mines


class Statement():

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def identified_mines(self):
        if self.count == len(self.cells):
            return self.cells

    def identified_safes(self):
        if self.count == 0:
            return self.cells

    def mark_mine(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1
        else:
            pass

    def mark_safe(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)
        else:
            pass


class AIForMinesweeper():

    def __init__(self, height=8, width=8):

        self.height = height
        self.width = width

        self.moves = set()

        self.mines = set()
        self.safes = set()

        self.knowledge = []

    def mark_mine(self, cell):
        self.mines.add(cell)
        for statement in self.knowledge:
            statement.mark_mine(cell)

    def mark_safe(self, cell):
        self.safes.add(cell)
        for statement in self.knowledge:
            statement.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """

        # mark the cell as one of the moves made in the game
        self.moves.add(cell)

        # mark the cell as a safe cell, updating any sequences that contain the cell as well
        self.mark_safe(cell)

        # add new sentence to AI knowledge base based on value of cell and count
        cells = set()
        count_cpy = copy.deepcopy(count)
        close_cells = self.find_adjacent_cells(cell)     # returns neighbour cells
        for adj_cell in close_cells:
            if adj_cell in self.mines:
                count_cpy -= 1
            if adj_cell not in self.mines | self.safes:
                cells.add(adj_cell)                           # only add cells that are of unknown state

        new_sentence = Statement(cells, count_cpy)           # prepare new sentence

        if len(new_sentence.cells) > 0:                 # add that sentence to knowledge only if it is not empty
            self.knowledge.append(new_sentence)

        # check sentences for new cells that could be marked as safe or as mine
        self.update_knowledge()

        self.additional_inference()

    def find_adjacent_cells(self, cell):
        """
        returns cell that are 1 cell away from cell passed in arg
        """
        # returns cells close to arg cell by 1 cell
        close_cells = set()
        for row in range(self.height):
            for column in range(self.width):
                if abs(cell[0] - row) <= 1 and abs(cell[1] - column) <= 1 and (row, column) != cell:
                    close_cells.add((row, column))
        return close_cells

    def update_knowledge(self):
        """
        check knowledge for new safes and mines, updates knowledge if possible
        """
        # copies the knowledge to operate on copy
        knowledge_copy = copy.deepcopy(self.knowledge)

        for statement in knowledge_copy:
            if len(statement.cells) == 0:
                try:
                    self.knowledge.remove(statement)
                except ValueError:
                    pass

            # check for possible mines and safes
            mines = statement.identified_mines()
            safes = statement.identified_safes()

            # update knowledge if mine or safe was found
            if mines:
                for mine in mines:
                    self.mark_mine(mine)
                    self.update_knowledge()
            if safes:
                for safe in safes:
                    self.mark_safe(safe)
                    self.update_knowledge()

    def additional_inference(self):
        """
        update knowledge based on inference
        """
        # iterate through pairs of sentences
        for statement1 in self.knowledge:
            for statement2 in self.knowledge:
                # check if sentence 1 is subset of sentence 2
                if statement1.cells.issubset(statement2.cells):
                    new_cells = statement2.cells - statement1.cells
                    new_count = statement2.count - statement1.count
                    new_sentence = Statement(new_cells, new_count)
                    mines = new_sentence.identified_mines()
                    safes = new_sentence.identified_safes()
                    if mines:
                        for mine in mines:
                            self.mark_mine(mine)

                    if safes:
                        for safe in safes:
                            self.mark_safe(safe)

    def make_safe_move(self):
        
        for cell in self.safes - self.moves:
            return cell
        
        return None

    def make_random_move(self):

        max_moves = self.width * self.height

        while max_moves > 0:
            max_moves -= 1

            row = random.randrange(self.height)
            column = random.randrange(self.width)

            if (row, column) not in self.moves | self.mines:
                return (row, column)

        return None
