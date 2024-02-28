import pytest
from Controllers.MatchController import MatchController


# Mock de la classe Match pour éviter les dépendances externes
class MockMatch:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


# Remplacement de la classe Match par MockMatch pour les tests
MatchController.Match = MockMatch


@pytest.fixture
def match_controller():
    return MatchController()


def test_create_match_pairs(match_controller):
    players = ['Joueur1', 'Joueur2', 'Joueur3', 'Joueur4']
    expected_pairs = [('Joueur1', 'Joueur2'), ('Joueur3', 'Joueur4')]
    assert match_controller.create_match_pairs(players) == expected_pairs


def test_create_matches(match_controller):
    pairs = [('Joueur1', 'Joueur2'), ('Joueur3', 'Joueur4')]
    matches = match_controller.create_matches(pairs)
    assert len(matches) == 2
    assert matches[0].player1 == 'Joueur1'
    assert matches[0].player2 == 'Joueur2'


def test_pair_players(match_controller):
    sorted_players = [
        {'first_name': 'Alice', 'last_name': 'Wonderland'},
        {'first_name': 'Bob', 'last_name': 'Builder'}
    ]
    played_matches = []
    expected_pairs = [(sorted_players[0], sorted_players[1])]
    assert match_controller.pair_players(sorted_players, played_matches) == expected_pairs


def test_has_played_together(match_controller):
    player1 = {'first_name': 'Alice', 'last_name': 'Wonderland'}
    player3 = {'first_name': 'Charlie', 'last_name': 'Chocolate'}
    played_matches = []
    assert not match_controller.has_played_together(player1, player3, played_matches)
