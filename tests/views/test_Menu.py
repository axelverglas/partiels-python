import pytest
from Views.Menu import Menu


@pytest.fixture
def menu():
    return Menu()


def test_main_menu(mocker, menu):
    # Simuler la réponse de l'utilisateur comme choisissant "1. Ajouter un joueur"
    mocker.patch('builtins.input', return_value='1')

    # Appeler la méthode main_menu et vérifier que le retour est "1"
    assert menu.main_menu() == '1'


def test_report_menu(mocker, menu):
    # Simuler la réponse de l'utilisateur comme choisissant "2. Liste des tous les Tournois"
    mocker.patch('builtins.input', return_value='2')

    # Appeler la méthode report_menu et vérifier que le retour est "2"
    assert menu.report_menu() == '2'
