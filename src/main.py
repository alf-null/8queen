import argparse
from n_queens import NQueens

parser = argparse.ArgumentParser()
parser.add_argument('size', help='This will be N number of queens')
args = parser.parse_args()
n = int(args.size) 

problem_solver = NQueens(n)
total_solutions = problem_solver.solver_helper()
print(f'The total of solution for {args.size} is: {total_solutions}')