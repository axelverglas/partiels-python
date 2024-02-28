import pytest
from unittest.mock import patch
from Controllers.MenuController import MenuController


@pytest.fixture
def menu_controller():
    return MenuController()


def test_user_choice_exit(menu_controller):

    with patch('builtins.input', return_value='0'):
        with patch('builtins.print') as mock_print:
            with pytest.raises(SystemExit):
                menu_controller.user_choice()
            mock_print.assert_called_with("Au revoir!")


def test_user_choice_invalid(menu_controller):

    with patch('builtins.input', side_effect=['9', '0']):  # '9' est invalide, suivi par '0' pour sortir
        with patch('builtins.print') as mock_print:
            with pytest.raises(SystemExit):
                menu_controller.user_choice()
            # Vérifiez si le message d'erreur spécifique est dans la liste des appels à print
            error_message_calls = [
                call for call in mock_print.call_args_list
                if "Choix non valide. Veuillez entrer un chiffre valide." in call[0][0]
            ]
            assert len(error_message_calls) > 0, "Le message d'erreur attendu n'a pas été trouvé."
