import pytest

from src import n_queens


def test_8_queen_result():
    n_queens.n_queen_solver(8, 0)
    assert len(n_queens.solutions) == 92