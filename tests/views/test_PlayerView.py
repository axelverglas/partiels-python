import pytest
from Views.PlayerView import PlayerView


@pytest.fixture
def player_view():
    return PlayerView()


def test_get_player_info(mocker, player_view):
    # Mock des méthodes pour simuler les entrées utilisateur
    mocker.patch.object(player_view, 'get_valid_alpha_input', side_effect=['John', 'Doe'])
    mocker.patch.object(player_view, 'get_valid_date_input', return_value='01/01/1990')
    mocker.patch('builtins.input', return_value='AB12345')
    mocker.patch.object(player_view, 'is_valid_id', return_value=True)

    first_name, last_name, birth_date, national_chess_id = player_view.get_player_info()

    assert first_name == 'John'
    assert last_name == 'Doe'
    assert birth_date == '01/01/1990'
    assert national_chess_id == 'AB12345'


def test_select_player(mocker, player_view):
    players = [
        {
            'first_name': 'John',
            'last_name': 'Doe',
            'birth_date': '01/01/1990',
            'national_chess_id': 'AB12345'
        },
        {
            'first_name': 'Jane',
            'last_name': 'Roe',
            'birth_date': '02/02/1992',
            'national_chess_id': 'CD67890'
        }
    ]
    # Simuler l'entrée utilisateur pour sélectionner le deuxième joueur (index 1)
    mocker.patch('builtins.input', return_value='2')

    selected_index = player_view.select_player(players)

    # Attendu : l'index du premier joueur dans la liste originale (inverse de l'affichage)
    assert selected_index == 0
