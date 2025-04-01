import pytest
from vacancy import Vacancy
from utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy(
            "Python Developer",
            "https://hh.ru/vacancy/1",
            {"from": 100000, "to": 150000, "currency": "RUR"},
            "Разработка на Python",
            "Опыт работы от 3 лет"
        ),
        Vacancy(
            "Java Developer",
            "https://hh.ru/vacancy/2",
            {"from": 120000, "to": 180000, "currency": "RUR"},
            "Разработка на Java",
            "Опыт работы от 5 лет"
        ),
        Vacancy(
            "JavaScript Developer",
            "https://hh.ru/vacancy/3",
            None,
            "Разработка на JavaScript",
            "Опыт работы от 2 лет"
        )
    ]


def test_filter_vacancies(sample_vacancies):
    filtered = filter_vacancies(sample_vacancies, ["Python"])
    assert len(filtered) == 1
    assert filtered[0].title == "Python Developer"

    filtered = filter_vacancies(sample_vacancies, [])
    assert len(filtered) == 3


def test_get_vacancies_by_salary(sample_vacancies):
    ranged = get_vacancies_by_salary(sample_vacancies, "110000-160000")
    assert len(ranged) == 2
    assert ranged[0].title == "Java Developer"
    assert ranged[1].title == "Python Developer"

    ranged = get_vacancies_by_salary(sample_vacancies, "")
    assert len(ranged) == 3


def test_sort_vacancies(sample_vacancies):
    sorted_vac = sort_vacancies(sample_vacancies)
    assert sorted_vac[0].title == "Java Developer"
    assert sorted_vac[1].title == "Python Developer"
    assert sorted_vac[2].title == "JavaScript Developer"


def test_get_top_vacancies(sample_vacancies):
    top = get_top_vacancies(sample_vacancies, 2)
    assert len(top) == 2
    assert top[0].title == "Java Developer"
    assert top[1].title == "Python Developer"