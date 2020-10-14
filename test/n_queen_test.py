import pytest

from src import n_queens


def test_8_queen_result():
    obj = n_queens.NQueens(8)
    assert obj.solver_helper() == 92