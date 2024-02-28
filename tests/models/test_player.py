import json
import pytest
from Models.Player import Player


@pytest.fixture
def player_instance(mocker):
    # Simuler get_new_id pour retourner un ID fixe
    mocker.patch('Models.Model.Model.get_new_id', return_value=1)
    # Initialiser une instance de Player sans interaction avec le système de fichiers
    player = Player("John", "Doe", "1990-01-01", "12345678")
    return player


def test_save_player_creates_file_if_not_exists(mocker, player_instance):
    # Simuler 'os.path.exists' pour retourner False, simulant un fichier inexistant
    mocker.patch('os.path.exists', return_value=False)
    # Utiliser mock_open pour simuler l'ouverture et l'écriture dans un fichier
    mock_file = mocker.mock_open()
    mocker.patch('builtins.open', mock_file)

    player_instance.save_player()

    # Vérifier si open a été appelé correctement pour écrire dans le fichier
    mock_file.assert_called_once_with('data/players.json', 'w')


def test_get_players_returns_list_of_players(mocker, player_instance):
    # Simuler des données de joueurs existantes
    players_data = json.dumps([
        {
            'id': 1,
            'first_name': 'Jane',
            'last_name': 'Doe',
            'birth_date': '1989-01-01',
            'national_chess_id': '87654321'
        }
    ])
    mocker.patch('builtins.open', mocker.mock_open(read_data=players_data))
    mocker.patch('os.path.exists', return_value=True)

    players = player_instance.get_players()

    # Vérifier que la méthode retourne une liste de joueurs
    assert isinstance(players, list), "get_players doit retourner une liste"
    assert len(players) == 1, "La liste des joueurs n'est pas correcte"
    assert players[0]['first_name'] == 'Jane', "Le joueur n'a pas été correctement récupéré"
