from copy import deepcopy

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY_SLOT = None


def starting_state():
    """
    Returns initial state of the game board.
    """
    return [[EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT],
            [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT],
            [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]]


def current_player(board):
    """
    Returns the player who is currently taking their turn.
    """
    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(PLAYER_X)
        o_count += row.count(PLAYER_O)

    if x_count <= o_count:
        return PLAYER_X
    else:
        return PLAYER_O


def available_moves(board):
    """
    Returns a set of all available moves (i, j) on the board.
    """

    available_moves_set = set()

    for row_index, row in enumerate(board):
        for column_index, item in enumerate(row):
            if item == None:
                available_moves_set.add((row_index, column_index))
    
    return available_moves_set


def move_result(board, move):
    """
    Returns the board that results from making the given move (i, j).
    """
    current_player_move = current_player(board)

    new_board = deepcopy(board)
    i, j = move

    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = current_player_move

    return new_board


def game_winner(board):
    """
    Determines if there's a winner in the current state of the game.
    Returns the winner (PLAYER_X or PLAYER_O), or None if there's no winner yet.
    """
    for player in (PLAYER_X, PLAYER_O):
        # Check vertical
        for row in board:
            if row == [player] * 3:
                return player

        # Check horizontal
        for i in range(3):
            column = [board[x][i] for x in range(3)]
            if column == [player] * 3:
                return player
        
        # Check diagonal
        if [board[i][i] for i in range(0, 3)] == [player] * 3:
            return player
        elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
            return player

    return None
                               

def game_over(board):
    """
    Determines if the game is over.
    Returns True if the game is over, False otherwise.
    """
    # Game is won by one of the players
    if game_winner(board) != None:
        return True

    # Moves are still possible
    for row in board:
        if EMPTY_SLOT in row:
            return False

    # No possible moves left
    return True


def game_result(board):
    """
    Determines the result of the game.
    Returns 1 if PLAYER_X has won, -1 if PLAYER_O has won, 0 otherwise.
    """
    win_player = game_winner(board)

    if win_player == PLAYER_X:
        return 1
    elif win_player == PLAYER_O:
        return -1
    else:
        return 0


def optimal_move(board):
    """
    Returns the optimal move for the current player on the board.
    """

    def max_value(board):
        optimal_move = ()
        if game_over(board):
            return game_result(board), optimal_move
        else:
            v = -5
            for move in available_moves(board):
                min_val = min_value(move_result(board, move))[0]
                if min_val > v:
                    v = min_val
                    optimal_move = move
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if game_over(board):
            return game_result(board), optimal_move
        else:
            v = 5
            for move in available_moves(board):
                max_val = max_value(move_result(board, move))[0]
                if max_val < v:
                    v = max_val
                    optimal_move = move
            return v, optimal_move

    current_player_turn = current_player(board)

    if game_over(board):
        return None

    if current_player_turn == PLAYER_X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
