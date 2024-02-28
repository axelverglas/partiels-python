import pytest
from Views.RoundsView import RoundsView


@pytest.fixture
def rounds_view():
    return RoundsView()


def test_ask_for_next_round_yes(mocker, rounds_view):
    mocker.patch("builtins.input", return_value="o")
    assert rounds_view.ask_for_next_round() == "o"


def test_ask_for_next_round_no(mocker, rounds_view):
    mocker.patch("builtins.input", return_value="n")
    assert rounds_view.ask_for_next_round() == "n"


def test_ask_for_next_round_trim_and_lower(mocker, rounds_view):
    mocker.patch("builtins.input", return_value=" O ")
    assert rounds_view.ask_for_next_round() == "o"
