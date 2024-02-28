from Controllers.TournamentController import TournamentController
import pytest


@pytest.fixture
def tournament_controller():
    return TournamentController()


def test_add_player_to_tournament(mocker, tournament_controller):
    # Mock des dépendances sur l'instance spécifique
    mock_tournament_view = mocker.patch.object(tournament_controller, 'tournamentView')
    mock_player_view = mocker.patch.object(tournament_controller, 'playerView')
    mocker.patch('builtins.input', return_value='n')
    mock_tournament = mocker.patch.object(tournament_controller, 'tournament')
    mock_player = mocker.patch.object(tournament_controller, 'player')

    # Configuration des mocks
    mock_tournament.get_tournaments.return_value = [{'id': 1, 'player_list': [], 'rounds': 4}]
    mock_player.get_players.return_value = [{'id': 'player1', 'name': 'John Doe'}]
    mock_tournament_view.select_tournament.return_value = 1
    mock_player_view.select_player.return_value = 0

    # Exécution de la méthode à tester
    tournament_controller.add_player_to_tournament()
