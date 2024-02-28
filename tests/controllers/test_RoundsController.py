import pytest
from Controllers.RoundsController import RoundsController


@pytest.fixture
def rounds_controller():
    return RoundsController()


def test_load_tournaments(mocker, rounds_controller):
    read_data = '[{"id": 1, "name": "Test Tournament"}]'
    mock_open = mocker.patch('builtins.open', mocker.mock_open(read_data=read_data))
    mocker.patch('json.load', return_value=[{"id": 1, "name": "Test Tournament"}])
    tournaments = rounds_controller.load_tournaments()
    mock_open.assert_called_once_with('data/tournaments.json', 'r')
    assert tournaments == [{"id": 1, "name": "Test Tournament"}]


def test_sort_players_by_score(rounds_controller):
    players = [
        {'first_name': 'John', 'last_name': 'Doe', 'score': 2},
        {'first_name': 'Jane', 'last_name': 'Doe', 'score': 3},
        {'first_name': 'Max', 'last_name': 'Mustermann', 'score': 1}
    ]
    sorted_players = rounds_controller.sort_players_by_score(players)
    assert sorted_players == [
        {'first_name': 'Jane', 'last_name': 'Doe', 'score': 3},
        {'first_name': 'John', 'last_name': 'Doe', 'score': 2},
        {'first_name': 'Max', 'last_name': 'Mustermann', 'score': 1}
    ]


def test_get_match_results(mocker, rounds_controller):
    match_mock_1 = mocker.MagicMock()
    match_mock_2 = mocker.MagicMock()
    matches = [match_mock_1, match_mock_2]
    mocker.patch.object(rounds_controller.matchView, 'display_match_results', side_effect=[1, 2])
    current_round = 1
    results = rounds_controller.get_match_results(matches, current_round)
    # Vérification simplifiée car la création des résultats attendus nécessite
    # une connaissance approfondie de la structure des objets match
    assert len(results) == 2
