import pytest

from src import application
from src.application import run
from src.grid import create_matrix


@pytest.fixture
def grid():
    return create_matrix()


def test_when_the_game_starts_should_display_grid_and_ask_player_to_choose_a_column(grid, mocker):
    mocker.patch("src.application.display_message")
    mocker.patch("src.application.get_column_from_user", return_value=1)
    run(grid)
    application.display_message.assert_any_call(grid, "X")


def test_when_column_value_given_should_insert_x_token_in_that_column(grid, mocker):
    mocker.patch("src.application.display_message")
    mocker.patch("src.application.get_column_from_user", return_value=1)
    mocker.patch("src.application.add_token")
    run(grid)
    application.add_token.assert_any_call(grid, 1, "X")


def test_when_o_turn_starts_display_grid_and_ask_player_to_choose_a_column(grid, mocker):
    mocker.patch("src.application.display_message")
    mocker.patch("src.application.get_column_from_user", return_value=1)
    run(grid)
    application.display_message.assert_any_call(grid, "O")


def test_when_column_value_given_should_insert_o_token_in_that_column(grid, mocker):
    mocker.patch("src.application.display_message")
    mocker.patch("src.application.get_column_from_user", return_value=1)
    mocker.patch("src.application.add_token")
    run(grid)
    application.add_token.assert_any_call(grid, 1, "O")


def test_when_x_is_the_winner_game_should_stop_and_display_x_is_the_winner(grid, mocker):
    mocker.patch("src.application.display_message")
    mocker.patch("src.application.get_column_from_user", return_value=1)
    mocker.patch("src.application.check_game_status", return_value="X")
    run(grid)
    application.display_message.assert_any_call(grid, "X is the winner")


def test_when_o_is_the_winner_game_should_stop_and_display_o_is_the_winner(grid, mocker):
    mocker.patch("src.application.display_message")
    mocker.patch("src.application.get_column_from_user", return_value=1)
    mocker.patch("src.application.check_game_status", return_value="O")
    run(grid)
    application.display_message.assert_any_call(grid, "O is the winner")


def test_when_there_is_a_draw_should_stop_and_display_draw(grid, mocker):
    mocker.patch("src.application.display_message")
    mocker.patch("src.application.get_column_from_user", return_value=1)
    mocker.patch("src.application.check_game_status", return_value="Draw")
    run(grid)
    application.display_message.assert_any_call(grid, "Draw")
