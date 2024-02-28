import json
from Models.Tournament import Tournament
import pytest


@pytest.fixture
def tournament_instance():
    return Tournament(name="Tournoi Test", location="Paris", start_date="01/01/2024", end_date="01/02/2024")


@pytest.fixture
def mock_json_data():
    return [
        {
            "id": 1,
            "name": "Tournoi Existant",
            "location": "Lyon",
            "start_date": "02/02/2024",
            "end_date": "02/03/2024",
            "rounds": 4,
            "current_round": 1,
            "round_list": [],
            "player_list": [],
            "description": ""
        }
    ]


def test_save_tournament(mocker, tournament_instance):
    mocker.patch('os.path.exists', return_value=False)
    mocker.patch('os.makedirs')
    mock_open = mocker.patch('builtins.open', mocker.mock_open())
    tournament_instance.save_tournament()
    mock_open.assert_called_once_with('data/tournaments.json', 'w')
    assert mock_open().write.call_count > 0  # Modifié ici


def test_get_tournaments(mocker, mock_json_data):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('builtins.open', mocker.mock_open(read_data=json.dumps(mock_json_data)))
    # Initialisation avec des valeurs factices
    tournaments = Tournament("Dummy", "Dummy", "01/01/2024", "01/02/2024").get_tournaments()
    assert tournaments == mock_json_data


def test_update_tournament(mocker, mock_json_data, tournament_instance):
    updated_tournament = mock_json_data[0]
    updated_tournament['name'] = "Tournoi Mis à Jour"
    mocker.patch('os.path.exists', return_value=True)
    # Simule à la fois la lecture avec des données JSON et l'écriture
    mock_open = mocker.patch('builtins.open', mocker.mock_open(read_data=json.dumps(mock_json_data)))
    tournament_instance.update_tournament(updated_tournament)
    mock_open.assert_called_with('data/tournaments.json', 'w')
