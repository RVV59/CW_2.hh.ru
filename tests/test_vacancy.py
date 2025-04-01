import pytest
from vacancy import Vacancy


@pytest.fixture
def sample_vacancies():
    vacancy1 = Vacancy(
        "Python Developer",
        "https://hh.ru/vacancy/1",
        {"from": 100000, "to": 150000, "currency": "RUR"},
        "Разработка на Python",
        "Опыт работы от 3 лет"
    )
    vacancy2 = Vacancy(
        "Java Developer",
        "https://hh.ru/vacancy/2",
        {"from": 120000, "to": 180000, "currency": "RUR"},
        "Разработка на Java",
        "Опыт работы от 5 лет"
    )
    vacancy3 = Vacancy(
        "JavaScript Developer",
        "https://hh.ru/vacancy/3",
        None,
        "Разработка на JavaScript",
        "Опыт работы от 2 лет"
    )
    return vacancy1, vacancy2, vacancy3


def test_vacancy_creation(sample_vacancies):
    vacancy1, _, _ = sample_vacancies
    assert vacancy1.title == "Python Developer"
    assert vacancy1.url == "https://hh.ru/vacancy/1"
    assert vacancy1.salary_from == 100000
    assert vacancy1.salary_to == 150000


def test_vacancy_comparison(sample_vacancies):
    vacancy1, vacancy2, _ = sample_vacancies
    assert vacancy1 < vacancy2
    assert vacancy2 > vacancy1
    assert not vacancy1 == vacancy2


def test_vacancy_without_salary(sample_vacancies):
    _, _, vacancy3 = sample_vacancies
    assert vacancy3.salary_from == 0
    assert vacancy3.salary_to == 0
    assert vacancy3.currency == "Не указана"


def test_vacancy_str(sample_vacancies):
    vacancy1, _, _ = sample_vacancies
    assert "Python Developer" in str(vacancy1)
    assert "100000 - 150000 RUR" in str(vacancy1)


def test_cast_to_object_list():
    vacancies_data = [{
        "name": "Python Developer",
        "alternate_url": "https://hh.ru/vacancy/1",
        "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
        "snippet": {
            "responsibility": "Разработка на Python",
            "requirement": "Опыт работы от 3 лет"
        }
    }]
    vacancies = Vacancy.cast_to_object_list(vacancies_data)
    assert len(vacancies) == 1
    assert vacancies[0].title == "Python Developer"