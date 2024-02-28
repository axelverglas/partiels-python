import json
import pytest
from Models.Model import Model


@pytest.fixture
def model():
    """Fixture pour créer une nouvelle instance de Model."""
    return Model()


def test_get_new_id_no_file(mocker, model):
    # Configuration du mock pour simuler l'absence de fichier
    mocker.patch('os.path.exists', return_value=False)

    assert model.get_new_id('fake_path.json') == 1, "Devrait retourner 1 si le fichier n'existe pas"


def test_get_new_id_empty_file(mocker, model):
    # Configuration des mocks pour simuler un fichier vide
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('builtins.open', mocker.mock_open(read_data='[]'))

    assert model.get_new_id('empty_file.json') == 1, "Devrait retourner 1 si le fichier est vide"


def test_get_new_id_with_data(mocker, model):
    # Création de fausses données pour le test
    data = json.dumps([{'id': 1}, {'id': 2}])
    # Configuration des mocks pour simuler un fichier avec des données
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('builtins.open', mocker.mock_open(read_data=data))

    expected_id = 3
    msg = "Devrait retourner l'ID suivant le dernier dans le fichier"
    assert model.get_new_id('data_file.json') == expected_id, msg
