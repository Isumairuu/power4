import pytest

from src.grid import *


@pytest.fixture(autouse=True)
def grid():
    return create_matrix()


def test_when_the_grid_is_initialized_should_return_dimension_6_by_7(grid):
    assert matrix_dimension(grid) == (6, 7)


def test_when_the_grid_is_initialized_should_return_a_6_by_7_matrix_of_points(grid):
    assert (grid == np.full((6, 7), ".")).all()


def test_when_we_insert_token_in_the_first_column_should_return_grid_with_the_new_token_in_the_first_column(grid):
    add_token(grid, 0, "X")
    column = get_column(grid, 0)
    assert column == [".", ".", ".", ".", ".", "X"]


def test_when_we_insert_token_in_a_full_column_should_return_index_error_exception(grid):
    for i in range(6):
        add_token(grid, 0, "X")
    with pytest.raises(InsertInAFullColumnException):
        add_token(grid, 0, "X")


def test_when_we_try_to_insert_token_in_a_column_that_is_out_of_bound_should_return_index_error_exception(grid):
    with pytest.raises(ColumnIndexOutOfRangeException):
        add_token(grid, -2, "X")
    with pytest.raises(ColumnIndexOutOfRangeException):
        add_token(grid, 8, "X")


def test_when_we_insert_a_token_should_be_inserted_at_the_end(grid):
    add_token(grid, 0, "X")
    column = get_column(grid, 0)
    assert column[-1] == "X" and column[0:-1] == ["." for i in range(5)]


def test_when_we_empty_the_grid_should_return_an_empty_grid(grid):
    for i in range(6):
        add_token(grid, i, "X")
    assert (np.full((6, 7), ".") == empty_grid()).all()


def test_when_we_print_an_empty_grid_should_return_correct_format(grid):
    assert display_grid(grid) == ('.  .  .  .  .  .  .\n'
                                  '.  .  .  .  .  .  .\n'
                                  '.  .  .  .  .  .  .\n'
                                  '.  .  .  .  .  .  .\n'
                                  '.  .  .  .  .  .  .\n'
                                  '.  .  .  .  .  .  .')


def test_when_we_print_a_grid_should_return_correct_format(grid):
    for i in range(2):
        add_token(grid, 0, "X")
        add_token(grid, 0, "O")
    for i in range(2):
        add_token(grid, 1, "O")
        add_token(grid, 1, "X")
    assert display_grid(grid) == ('.  .  .  .  .  .  .\n'
                                  '.  .  .  .  .  .  .\n'
                                  'O  X  .  .  .  .  .\n'
                                  'X  O  .  .  .  .  .\n'
                                  'O  X  .  .  .  .  .\n'
                                  'X  O  .  .  .  .  .')


def test_when_we_print_a_full_grid_should_return_correct_format(grid):
    for i in range(7):
        for _ in range(6):
            add_token(grid, i, "X")

    assert display_grid(grid) == ('X  X  X  X  X  X  X\n'
                                  'X  X  X  X  X  X  X\n'
                                  'X  X  X  X  X  X  X\n'
                                  'X  X  X  X  X  X  X\n'
                                  'X  X  X  X  X  X  X\n'
                                  'X  X  X  X  X  X  X')


# def test_diags(grid):
#     assert get_diagonals(grid) == ['.  .  .  .',
#                                    '.  .  .  .',
#                                    '.  .  .  .  .',
#                                    '.  .  .  .  .',
#                                    '.  .  .  .  .  .',
#                                    '.  .  .  .  .  .',
#                                    '.  .  .  .  .  .',
#                                    '.  .  .  .  .  .',
#                                    '.  .  .  .  .',
#                                    '.  .  .  .  .',
#                                    '.  .  .  .',
#                                    '.  .  .  .']
