import pytest

from src import n_queens

@pytest.fixture()
def db_table(mocker):
    create_engine = mocker.patch('sqlalchemy.create_engine').return_value
    create_engine.connect.return_value.execute.return_value = None


def test_8_queen_result(db_table):
    obj = n_queens.NQueens(8)
    assert obj.solver_helper() == 92