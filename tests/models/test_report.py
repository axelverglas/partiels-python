from Models.Report import Report


def test_load_players_with_empty_file(mocker):
    # Simulation de l'ouverture du fichier players.json avec des données vides
    mocker.patch('builtins.open', mocker.mock_open(read_data='[]'))
    mocker.patch('os.path.exists', return_value=True)

    report = Report()
    assert report.players == [], "La liste des joueurs devrait être vide"


def test_load_players_file_not_found(mocker):
    # Simulation de l'erreur FileNotFoundError lors de l'ouverture du fichier players.json
    mocker.patch('builtins.open', mocker.mock_open())
    mocker.patch('builtins.open', side_effect=FileNotFoundError)

    report = Report()
    assert report.players == [], "La liste des joueurs devrait être vide en cas de fichier non trouvé"


def test_load_tournaments_with_empty_file(mocker):
    # Simulation de l'ouverture du fichier tournaments.json avec des données vides
    mocker.patch('builtins.open', mocker.mock_open(read_data='[]'))
    mocker.patch('os.path.exists', return_value=True)

    report = Report()
    assert report.tournaments == [], "La liste des tournois devrait être vide"


def test_load_tournaments_file_not_found(mocker):
    # Simulation de l'erreur FileNotFoundError lors de l'ouverture du fichier tournaments.json
    mocker.patch('builtins.open', mocker.mock_open())
    mocker.patch('builtins.open', side_effect=FileNotFoundError)

    report = Report()
    assert report.tournaments == [], "La liste des tournois devrait être vide en cas de fichier non trouvé"


def test_load_players_json_decode_error(mocker):
    # Simulation d'une erreur de décodage JSON lors de la lecture du fichier players.json
    mocker.patch('builtins.open', mocker.mock_open(read_data='{non valide json'))
    mocker.patch('os.path.exists', return_value=True)

    report = Report()
    assert report.players == [], "La liste des joueurs devrait être vide en cas d'erreur de décodage JSON"
