import numpy as np

from src.grid import get_rows, get_columns, get_diagonals


def check_game_status(grid: np.ndarray):
    lines = get_rows(grid) or get_columns(grid) or get_diagonals(grid)
    if lines:
        for line in lines:
            if "X  X  X  X" in line:
                return "X"
            if "O  O  O  O" in line:
                return "O"
    if "." not in grid:
        return "Draw"
