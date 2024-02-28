import pytest
from Models.Match import Match


@pytest.fixture
def player1():
    return {'first_name': 'John', 'last_name': 'Doe', 'score': 0}


@pytest.fixture
def player2():
    return {'first_name': 'Jane', 'last_name': 'Roe', 'score': 0}


@pytest.fixture
def match(player1, player2):
    return Match(player1, player2)


def test_match_serialize(match, player1, player2):
    # Définition du gagnant pour le test
    match.winner = player1

    # Test de la méthode serialize
    expected_output = {
        'player1': player1,
        'player2': player2,
        'winner': player1
    }
    assert match.serialize() == expected_output, "La méthode serialize ne fonctionne pas comme prévu."


def test_match_str(match):
    # Test de la méthode __str__
    expected_str = "John Doe VS Jane Roe"
    assert str(match) == expected_str, "La méthode __str__ ne retourne pas la chaîne attendue."
