import pytest
from Views.TournamentView import TournamentView


@pytest.fixture
def tournament_view():
    return TournamentView()


def test_get_tournament_info(mocker, tournament_view):
    mocker.patch.object(tournament_view, 'get_valid_alpha_input', side_effect=['Tournoi Test', 'Paris'])
    mocker.patch.object(tournament_view, 'get_valid_date_input', side_effect=['01/01/2024', '05/01/2024'])
    mocker.patch.object(tournament_view, 'get_valid_int_input', return_value=4)
    mocker.patch('builtins.input', return_value='Description Test')

    expected = ('Tournoi Test', 'Paris', '01/01/2024', '05/01/2024', 4, 'Description Test')
    assert tournament_view.get_tournament_info() == expected


def test_select_tournament(mocker, tournament_view):
    mocker.patch('builtins.print')
    mocker.patch('builtins.input', return_value='1')

    tournaments = [
        {
            'id': 1,
            'name': 'Tournoi 1',
            'location': 'Paris',
            'start_date': '01/01/2024',
            'end_date': '05/01/2024',
            'rounds': 4,
        },
        {
            'id': 2,
            'name': 'Tournoi 2',
            'location': 'Lyon',
            'start_date': '10/02/2024',
            'end_date': '15/02/2024',
            'rounds': 4,
        }
      ]

    assert tournament_view.select_tournament(tournaments) == 2
