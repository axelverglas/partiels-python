import pytest
from Views.ReportView import ReportView


@pytest.fixture
def mock_print(mocker):
    return mocker.patch("builtins.print")


@pytest.fixture
def report_view():
    return ReportView()


@pytest.fixture
def sample_players():
    return [
        {'last_name': 'Doe', 'first_name': 'John', 'national_chess_id': '12345'},
        {'last_name': 'Smith', 'first_name': 'Jane', 'national_chess_id': '67890'},
    ]


@pytest.fixture
def sample_tournament():
    return {
        'name': 'Championnat du monde',
        'location': 'Paris',
        'start_date': '2024-01-01',
        'end_date': '2024-01-10'
    }


def test_display_players_alphabetical(report_view, sample_players, mock_print):
    report_view.display_players_alphabetical(sample_players)
    mock_print.assert_any_call("\nListe des joueurs par ordre alphabétique:")
    mock_print.assert_any_call("Doe John (INE: 12345)")
    mock_print.assert_any_call("Smith Jane (INE: 67890)")


def test_display_tournament_infos(report_view, sample_tournament, mock_print):
    report_view.display_tournament_infos(sample_tournament)
    mock_print.assert_any_call("\nDétails du tournoi :")
    mock_print.assert_any_call("Nom: Championnat du monde")
    mock_print.assert_any_call("Lieu: Paris")
    mock_print.assert_any_call("Date de début: 2024-01-01")
    mock_print.assert_any_call("Date de fin: 2024-01-10")
