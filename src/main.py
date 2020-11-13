import argparse
from n_queens import solver_helper

parser = argparse.ArgumentParser()
parser.add_argument("size", help="This will be N number of queens")
args = parser.parse_args()
n = int(args.size)

total_solutions = len(solver_helper(n))
print(f"The total of solution for {args.size} is: {total_solutions}")
