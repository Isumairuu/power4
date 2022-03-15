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


def empty_grid():
    return create_matrix()


def display_grid(matrix: np.ndarray):
    for line in matrix:
        print('  '.join(map(str, line)))
