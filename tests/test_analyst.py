import numpy as np
import pytest

from src.analyst import check_game_status
from src.grid import create_matrix

COLUMNS = ['.  .  .  .  .  .  .',
           '.  .  .  O  O  O  O',
           '.  .  .  .  .  .  .',
           '.  .  .  .  .  .  .',
           '.  .  .  .  .  .  .',
           '.  .  .  .  .  .  .']
ROWS = ['.  .  X  X  X  X',
        '.  .  .  .  .  .',
        '.  .  .  .  .  .',
        '.  .  .  .  .  .',
        '.  .  .  .  .  .',
        '.  .  .  .  .  .',
        '.  .  .  .  .  .']

DIAGONALS = ['.  .  .  .',
             '.  .  .  .',
             '.  .  .  .  .',
             '.  .  .  .  .',
             '.  .  .  .  .  .',
             '.  X  X  X  X  .',
             '.  .  .  .  .  .',
             '.  .  .  .  .  .',
             '.  .  .  .  .',
             '.  .  .  .  .',
             '.  .  .  .',
             '.  .  .  .']

FULL_GRID = [['X', 'X', 'X', 'O', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'O', 'X', 'O', 'O'],
             ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
             ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
             ['X', 'X', 'O', 'X', 'O', 'X', 'O'],
             ['O', 'X', 'X', 'O', 'X', 'O', 'X']]


@pytest.fixture
def grid():
    return create_matrix()


def test_when_given_a_grid_where_a_row_has_4_serial_x_tokens_should_return_x(mocker, grid):
    mocker.patch("src.analyser.get_rows", return_value=ROWS)
    expected = "X"
    actual = check_game_status(grid)
    assert actual == expected


def test_when_given_a_grid_where_a_column_has_4_serial_o_tokens_should_return_o(mocker, grid):
    mocker.patch("src.analyser.get_columns", return_value=COLUMNS)
    expected = "O"
    actual = check_game_status(grid)
    assert actual == expected


def test_when_given_a_grid_where_a_diagonal_has_4_serial_x_tokens_should_return_x(mocker, grid):
    mocker.patch("src.analyser.get_diagonals", return_value=ROWS)
    expected = "X"
    actual = check_game_status(grid)
    assert actual == expected


def test_when_given_a_full_grid_with_no_win_case_should_return_draw():
    assert check_game_status(np.array(FULL_GRID)) == "Draw"
