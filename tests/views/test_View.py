import pytest
from Views.View import View


@pytest.fixture
def view():
    return View()


def test_is_valid_alpha(view):
    assert view.is_valid_alpha("Test") is True
    assert view.is_valid_alpha("Test 123") is False
    assert view.is_valid_alpha("T") is False
    assert view.is_valid_alpha("Testé") is True


def test_get_valid_date_input(mocker, view):
    mocker.patch('builtins.input', side_effect=['31/02/2020', '01/01/2020'])
    mocker.patch.object(view, 'is_valid_date', side_effect=[False, True])
    assert view.get_valid_date_input("Date: ") == '01/01/2020'


def test_get_valid_alpha_input(mocker, view):
    mocker.patch('builtins.input', side_effect=['123', 'Test'])
    assert view.get_valid_alpha_input("Nom: ") == 'Test'


def test_get_valid_int_input_with_default(mocker, view):
    mocker.patch('builtins.input', return_value='')
    assert view.get_valid_int_input("Nombre de tours (optionnel, défaut à 4): ", 4) == 4


def test_get_valid_int_input_without_default(mocker, view):
    mocker.patch('builtins.input', side_effect=['abc', '5'])
    assert view.get_valid_int_input("Nombre: ") == 5
