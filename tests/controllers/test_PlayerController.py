import pytest
from Controllers.PlayerController import PlayerController
from Models.Player import Player
from Views.PlayerView import PlayerView


@pytest.fixture
def player_controller():
    return PlayerController()


def test_add_player(mocker, player_controller):
    player_info = ("John", "Doe", "1990-01-01", "12345678")

    mocked_get_player_info = mocker.patch.object(PlayerView, 'get_player_info', return_value=player_info)
    mocked_save_player = mocker.patch.object(Player, 'save_player')

    # Exécution de add_player en utilisant l'instance de PlayerController fournie par la fixture
    player_controller.add_player()

    # Vérifications
    mocked_get_player_info.assert_called_once()
    mocked_save_player.assert_called_once()

    # Vérification des attributs de l'instance player dans PlayerController
    assert player_controller.player.first_name == "John"
    assert player_controller.player.last_name == "Doe"
    assert player_controller.player.birth_date == "1990-01-01"
    assert player_controller.player.national_chess_id == "12345678"
