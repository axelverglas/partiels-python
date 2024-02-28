import pytest
from Controllers.ReportController import ReportController


@pytest.fixture
def report_controller():
    return ReportController()


def test_players_alphabetical(mocker, report_controller):
    mocker.patch('Models.Report.Report.load_players', return_value=[
        {'last_name': 'Doe', 'first_name': 'John'},
        {'last_name': 'Smith', 'first_name': 'Jane'},
        {'last_name': 'Doe', 'first_name': 'Alice'}
    ])

    sorted_players = report_controller.players_alphabetical()

    assert sorted_players == [
        {'last_name': 'Doe', 'first_name': 'Alice'},
        {'last_name': 'Doe', 'first_name': 'John'},
        {'last_name': 'Smith', 'first_name': 'Jane'}
    ]


def test_list_tournaments(mocker, report_controller):
    expected_tournaments = [
        {'name': 'Tournament A', 'id': 1},
        {'name': 'Tournament B', 'id': 2}
    ]

    mocker.patch('Models.Report.Report.load_tournaments', return_value=expected_tournaments)

    tournaments = report_controller.list_tournaments()

    assert tournaments == expected_tournaments


def test_select_tournament_from_list(mocker, report_controller):
    mocker.patch('Models.Report.Report.load_tournaments', return_value=[
        {'name': 'Tournament A', 'id': 1},
        {'name': 'Tournament B', 'id': 2}
    ])
    mocker.patch('builtins.input', return_value='1')

    selected_tournament = report_controller.select_tournament_from_list()

    assert selected_tournament == {'name': 'Tournament A', 'id': 1}


def test_tournament_players_alphabetical(mocker, report_controller):
    mocker.patch('Controllers.ReportController.ReportController.select_tournament_from_list', return_value={
        'player_list': [
            {'last_name': 'Doe', 'first_name': 'John', 'score': 3},
            {'last_name': 'Smith', 'first_name': 'Jane', 'score': 5},
            {'last_name': 'Doe', 'first_name': 'Alice', 'score': 2}
        ]
    })

    sorted_players = report_controller.tournament_players_alphabetical()

    assert sorted_players == [
        {'last_name': 'Doe', 'first_name': 'Alice', 'score': 2},
        {'last_name': 'Doe', 'first_name': 'John', 'score': 3},
        {'last_name': 'Smith', 'first_name': 'Jane', 'score': 5}
    ]


def test_get_tournament_players_sorted(mocker, report_controller):
    mocker.patch('Models.Report.Report.load_tournaments', return_value=[
        {
            'id': 1,
            'name': 'Tournament A',
            'player_list': [
                {'name': 'John Doe', 'score': 3},
                {'name': 'Jane Smith', 'score': 5},
                {'name': 'Alice Doe', 'score': 2}
            ]
        }
    ])

    sorted_players = report_controller.get_tournament_players_sorted(1)

    assert sorted_players == [
        {'name': 'Jane Smith', 'score': 5},
        {'name': 'John Doe', 'score': 3},
        {'name': 'Alice Doe', 'score': 2}
    ]
