
solutions = []


def is_possible(n, row, col, board):
    """
    Validates if the current position is suitable for placing a queen in a not-attacking position
    :param n: size of the board
    :param row: the current row
    :param col: the current col
    :return: True if the possition is a safe one
    """
    
    # Check column
    for i in range(n):
        if board[i][col] == 1:
            return False

    # Check upper left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def n_queen_solver(n, row, board=None):
    """
    Recursive function for placing queens on the board. It works  
    by using backtrancing: if in the current possition, does not
    contains the totally of the queens it reset the board and try again.

    :param n: size of the board
    :param row: the actual row of working (it will start at 0)
    """

    if board is None:
        board = [[0]*n for _ in range(n)]

    if row == n:
        solutions.append(board)
        return True

    for j in range(n):      
        if is_possible(n, row, j, board):
            board[row][j] = 1
            n_queen_solver(n, row + 1, board)
        
        board[row][j] = 0
