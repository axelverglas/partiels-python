import pytest
from Views.MatchView import MatchView


@pytest.fixture
def match_view():
    return MatchView()


@pytest.fixture
def mock_match(mocker):
    match = mocker.Mock()
    match.player1 = {'first_name': 'Alice', 'last_name': 'Wonderland'}
    match.player2 = {'first_name': 'Bob', 'last_name': 'Builder'}
    return match


def test_display_match_results_user_chooses_winner(mocker, match_view, mock_match):
    mocker.patch('builtins.input', return_value='1')

    # Appeler la méthode et vérifier le résultat
    result = match_view.display_match_results(mock_match, 1, 1)
    assert result == 1


def test_display_match_results_user_chooses_draw(mocker, match_view, mock_match):
    mocker.patch('builtins.input', return_value='3')

    result = match_view.display_match_results(mock_match, 1, 1)
    assert result == 3
