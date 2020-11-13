from models import Solution
from config import session
from copy import copy


def solver_helper(size):
    """Solve the n queens puzzle and print the number of solutions"""
    board = [-1 for _ in range(size)]
    solutions = []
    put_queen(board, solutions, 0)

    session.bulk_save_objects(
        [
            Solution(
                size=size,
                board=board,
            )
            for board in solutions
        ]
    )
    session.commit()

    return solutions


def put_queen(board, solutions, row):
    """
    Recursive function for placing queens on the board. It works
    by using backtrancing: if in the current possition, does not
    contains the totally of the queens it reset the board and try again.

    :param row: the actual row of working (it will start at 0)
    """
    if row == len(board):
        solutions.append(copy(board))
    else:
        for column in range(len(board)):
            if is_possible(board, row, column):
                board[row] = column
                put_queen(board, solutions, row + 1)


def is_possible(board, rows, column):
    """
    Validates if the current position is suitable for placing a queen in a not-attacking position
    only check diagonally
    :param row: the current row
    :param col: the current col
    :return: True if the possition is a safe one
    """
    for i in range(rows):
        if (
            board[i] == column
            or board[i] - i == column - rows
            or board[i] + i == column + rows
        ):

            return False
    return True
