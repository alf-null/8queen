class NQueens:    

    def __init__(self, n):
        self.board_size = n
        self.board = [[0]*n for _ in range(n)]
        self.solutions = []

    def is_possible(self, n, row, col):
        """
        Validates if the current position is suitable for placing a queen in a not-attacking position
        :param n: size of the board
        :param row: the current row
        :param col: the current col
        :return: True if the possition is a safe one
        """
        
        # Check column
        for i in range(n):
            if self.board[i][col] == 1:
                return False

        # Check upper left
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check upper right
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if self.board[i][j] == 1:
                return False

        return True


    def n_queen_solver(self, n, row):
        """
        Recursive function for placing queens on the board. It works  
        by using backtrancing: if in the current possition, does not
        contains the totally of the queens it reset the board and try again.

        :param n: size of the board
        :param row: the actual row of working (it will start at 0)
        """

        if row == n:
            self.solutions.append(self.board)
            return 

        for j in range(n):      
            if self.is_possible(n, row, j):
                self.board[row][j] = 1
                self.n_queen_solver(n, row + 1)
            
            self.board[row][j] = 0

    def solver_helper(self):
        self.n_queen_solver(self.board_size, 0)
        solutions = len(self.solutions)
        self.solutions = [
            [0] *self.board_size 
            for _ in range(self.board_size)
        ] 
        return solutions

obj = NQueens(8)
obj.solver_helper()