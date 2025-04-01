import pytest
import os
import json
from json_saver import JSONSaver


@pytest.fixture
def json_saver(tmp_path):
    filename = tmp_path / "test_vacancies.json"
    return JSONSaver(str(filename))


@pytest.fixture
def test_vacancy():
    return {
        "title": "Test Developer",
        "url": "https://hh.ru/vacancy/test",
        "salary_from": 100000,
        "salary_to": 150000,
        "currency": "RUR",
        "description": "Test description",
        "requirements": "Test requirements"
    }


def test_add_vacancy(json_saver, test_vacancy):
    json_saver.add_vacancy(test_vacancy)
    vacancies = json_saver.get_vacancies({})
    assert len(vacancies) == 1
    assert vacancies[0]["title"] == "Test Developer"


def test_no_duplicates(json_saver, test_vacancy):
    json_saver.add_vacancy(test_vacancy)
    json_saver.add_vacancy(test_vacancy)
    vacancies = json_saver.get_vacancies({})
    assert len(vacancies) == 1


def test_delete_vacancy(json_saver, test_vacancy):
    json_saver.add_vacancy(test_vacancy)
    json_saver.delete_vacancy(test_vacancy)
    vacancies = json_saver.get_vacancies({})
    assert len(vacancies) == 0


def test_filter_vacancies(json_saver, test_vacancy):
    json_saver.add_vacancy(test_vacancy)
    vacancies = json_saver.get_vacancies({"title": "Test"})
    assert len(vacancies) == 1
    vacancies = json_saver.get_vacancies({"title": "Nonexistent"})
    assert len(vacancies) == 0