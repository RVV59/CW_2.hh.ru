import pytest
from typing import List
from src.utils import (
    filter_vacancies,
    get_vacancies_by_salary,
    sort_vacancies,
    get_top_vacancies
)


# Фикстура с тестовыми вакансиями
@pytest.fixture
def sample_vacancies():
    return [
        Vacancy(
            title="Python Developer",
            description="Разработка на Python и Django",
            requirements="Опыт работы от 3 лет",
            salary_from=100000,
            salary_to=150000
        ),
        Vacancy(
            title="Java Developer",
            description="Разработка на Java и Spring",
            requirements="Опыт работы от 2 лет",
            salary_from=90000,
            salary_to=120000
        ),
        Vacancy(
            title="Data Scientist",
            description="Анализ данных с использованием Python",
            requirements="Знание Pandas, NumPy",
            salary_from=120000,
            salary_to=180000
        ),
        Vacancy(
            title="DevOps Engineer",
            description="Настройка CI/CD",
            requirements="Опыт с Docker, Kubernetes",
            salary_from=110000,
            salary_to=None  # Зарплата "до" не указана
        )
    ]


class Vacancy:
    def __init__(self, title, description, requirements, salary_from, salary_to):
        self.title = title
        self.description = description
        self.requirements = requirements
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __repr__(self):
        return f"Vacancy({self.title}, {self.salary_from}-{self.salary_to})"


# Тесты для filter_vacancies
def test_filter_vacancies_no_keywords(sample_vacancies):
    result = filter_vacancies(sample_vacancies, [])
    assert result == sample_vacancies


def test_filter_vacancies_with_keywords(sample_vacancies):
    result = filter_vacancies(sample_vacancies, ["Python"])
    assert len(result) == 2
    assert all("Python" in (v.description + v.requirements) for v in result)


def test_filter_vacancies_case_insensitive(sample_vacancies):
    result = filter_vacancies(sample_vacancies, ["python"])
    assert len(result) == 2


# Тесты для get_vacancies_by_salary
def test_get_vacancies_by_salary_no_range(sample_vacancies):
    result = get_vacancies_by_salary(sample_vacancies, "")
    assert result == sample_vacancies


def test_get_vacancies_by_salary_with_range(sample_vacancies):
    result = get_vacancies_by_salary(sample_vacancies, "100000-150000")
    assert len(result) == 2
    assert all(v.salary_from >= 100000 for v in result)
    # Проверяем что salary_to либо <= 150000, либо не указан
    assert all(v.salary_to <= 150000 if v.salary_to else True for v in result)


def test_get_vacancies_by_salary_invalid_range(sample_vacancies):
    result = get_vacancies_by_salary(sample_vacancies, "invalid-range")
    assert result == sample_vacancies


# Тесты для sort_vacancies
def test_sort_vacancies(sample_vacancies):
    sorted_list = sort_vacancies(sample_vacancies)
    salaries = [v.salary_from for v in sorted_list]
    assert salaries == [120000, 110000, 100000, 90000]
    assert sorted_list[0].title == "Data Scientist"
    assert sorted_list[-1].title == "Java Developer"


# Тесты для get_top_vacancies
def test_get_top_vacancies(sample_vacancies):
    top_2 = get_top_vacancies(sample_vacancies, 2)
    assert len(top_2) == 2
    assert top_2[0].title == "Python Developer"  # До сортировки первый элемент - Python Developer


def test_get_top_vacancies_more_than_exists(sample_vacancies):
    top_10 = get_top_vacancies(sample_vacancies, 10)
    assert len(top_10) == 4