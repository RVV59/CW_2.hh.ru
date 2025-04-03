import pytest
from src.storage import JSONSaver
from src.vacancy import Vacancy

@pytest.fixture
def json_saver():
    return JSONSaver("tests/test_vacancies.json")

@pytest.fixture
def vacancy():
    return Vacancy("Python Developer", "url1", {"from": 100000, "to": 150000, "currency": "RUR"}, "Описание 1", "Требования 1")

def test_add_vacancy(json_saver, vacancy):
    json_saver.add_vacancy(vacancy)
    vacancies = json_saver.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0]["title"] == "Python Developer"

def test_get_vacancies(json_saver, vacancy):
    json_saver.add_vacancy(vacancy)
    vacancies = json_saver.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0]["title"] == "Python Developer"

def test_delete_vacancy(json_saver, vacancy):
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)
    vacancies = json_saver.get_vacancies()
    assert len(vacancies) == 0