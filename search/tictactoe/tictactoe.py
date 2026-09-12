"""
Tic Tac Toe Player
"""

import copy
import math
from queue import Empty

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0

    for row in board:
        x += row.count(X)
        o += row.count(O)


    return O if x > o else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_moves = set()

    # need looop over x,y
    for i in range(len(board)):
        for j in range(len(board[i])):

            if board[i][j] == EMPTY:
                possible_moves.add((i,j))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    replica_board = copy.deepcopy(board)


    if player(replica_board) == X:
        symbol = X
    else:
        symbol = O

    # EXXTRA, cases
    if (action[0] < 0 or action[0] > 2) or (action[1] < 0 or action[1] > 2):
        raise Exception('Not a valid action for the board')

    if replica_board[action[0]][action[1]] == EMPTY:
        replica_board[action[0]][action[1]] = symbol
    else:
        raise Exception('Space already filled')

    return replica_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # X win

    # Over [x][y] in line
    for i in range(3):
        if all(board[i][j] == X for j in range(3)):
            return X
    for j in range(3):
        if all(board[i][j] == X for i in range(3)):
            return X

    # In cross
    if board[0][0]== X and board[1][1] == X and board [2][2] == X:
        return X
    if board[0][2]== X and board[1][1] == X and board [2][0] == X:
        return X


    # same thing that X, but just change to 0
    # O win
    # Over [x][y] in line
    for i in range(3):
        if all(board[i][j] == O for j in range(3)):
            return O
    for j in range(3):
        if all(board[i][j] == O for i in range(3)):
            return O

    # In cross
    if board[0][0]== O and board[1][1] == O and board [2][2] == O:
        return O
    if board[0][2]== O and board[1][1] == O and board [2][0] == O:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    if any(row.count(EMPTY) > 0 for row in board):
        return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    champion = winner(board)
    if champion == X:
        return 1
    elif champion == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    current_player = player(board)



    if current_player == X:
        best_score = -math.inf
        best_action = None


        for action in actions(board):
            score = minimax_value(result(board, action))

            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    else:
        best_score = math.inf
        best_action = None

        for action in actions(board):
            score = minimax_value(result(board, action))

            if score < best_score:
                best_score = score
                best_action = action

        return best_action




def minimax_value(board):
    # retunr the utility value of a board assuming both player play good
    #   I needed, almsot same behavior that the other function.

    if terminal(board):
        return utility(board)

    if player(board) == X:
        best_score = -math.inf

        for action in actions(board):
            score = minimax_value(result(board, action))
            best_score = max(best_score, score)

        return best_score



    else:
        best_score = math.inf
        for action in actions(board):
            score = minimax_value(result(board, action))
            best_score = min(best_score, score)
        return best_score
