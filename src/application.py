import numpy as np

from src.analyst import check_game_status
from src.grid import add_token
from src.view import display_message, get_column_from_user


def run(grid: np.ndarray):
    # while True:
    display_message(grid, "X")
    col = get_column_from_user()
    add_token(grid, col, "X")
    if check_game_status(grid) == "X":
        display_message(grid, "X is the winner")
        # break
    elif check_game_status(grid) == "Draw":
        display_message(grid, "Draw")
        # break
    else:
        display_message(grid, "O")
        col = get_column_from_user()
        add_token(grid, col, "O")
        if check_game_status(grid) == "O":
            display_message(grid, "O is the winner")
            # break
        if check_game_status(grid) == "Draw":
            display_message(grid, "Draw")
            # break
