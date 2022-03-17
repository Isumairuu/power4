import numpy as np


class ColumnIndexOutOfRangeException(IndexError):
    pass


class InsertInAFullColumnException(IndexError):
    pass


def create_matrix() -> np.ndarray:
    return np.full((6, 7), ".", str)


def add_token(matrix: np.ndarray, index: int, token: str):
    if index > 7 or index < 0:
        raise ColumnIndexOutOfRangeException("Column must be between 0 and 7")
    column = list(matrix[:, index])
    column.reverse()
    for i in range(6):
        if column[i] == ".":
            column[i] = token
            break
    column.reverse()
    if list(matrix[:, index]) == column:
        raise InsertInAFullColumnException("The column where you tried to insert the token is full")
    else:
        matrix[:, index] = column


def matrix_dimension(matrix: np.ndarray) -> (int, int):
    return matrix.shape


def get_column(matrix: np.ndarray, index: int) -> list:
    return list(matrix[:, index])


def get_rows(grid):
    pass


def get_columns(grid):
    pass


def get_diagonals(grid):
    pass


# def get_diagonals(grid):
#     diagonals = []
#     dim = len(grid[0])
#     for i in range(-dim + 2, dim - 1):
#         if len(grid.diagonal(i)) > 3:
#             diagonals.append("  ".join(grid.diagonal(i)))
#         if len(np.fliplr(grid).diagonal(i)) > 3:
#             diagonals.append("  ".join(np.fliplr(grid).diagonal(i)))
#     print(diagonals)
#     return diagonals

#
# def get_list_of_columns(matrix: np.ndarray, index: int) -> list:
#     columns = []
#     for i in range(matrix.shape[0]):
#         columns.append(list(matrix[:, index]))
#     return columns
#
#
# def get_list_of_rows(matrix: np.ndarray, index: int) -> list:
#     return list(matrix[index])
#
#
# def get_main_diagonals(matrix: np.ndarray, index: int) -> list:
#     return list(matrix.diagonal(index))
#
#
# def get_anti_diagonal(matrix: np.ndarray, index: int) -> list:
#     return list(matrix.diagonal(index))


def empty_grid():
    return create_matrix()


def display_grid(matrix: np.ndarray):
    return '\n'.join(['  '.join(['{}'.format(item) for item in row])
                      for row in matrix])
