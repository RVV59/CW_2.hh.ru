import pytest
from src.vacancy import Vacancy

@pytest.fixture
def vacancy_data():
    return {
        "name": "Python Developer",
        "alternate_url": "https://hh.ru/vacancy/123456",
        "salary": {
            "from": 100000,
            "to": 150000,
            "currency": "RUR"
        },
        "snippet": {
            "responsibility": "Разработка на Python",
            "requirement": "Опыт работы с Python"
        }
    }

@pytest.fixture
def vacancy(vacancy_data):
    return Vacancy(
        title=vacancy_data["name"],
        url=vacancy_data["alternate_url"],
        salary=vacancy_data["salary"],
        description=vacancy_data["snippet"]["responsibility"],
        requirements=vacancy_data["snippet"]["requirement"]
    )

def test_init(vacancy, vacancy_data):
    assert vacancy.title == vacancy_data["name"]
    assert vacancy.url == vacancy_data["alternate_url"]
    assert vacancy.salary_from == vacancy_data["salary"]["from"]
    assert vacancy.salary_to == vacancy_data["salary"]["to"]
    assert vacancy.currency == vacancy_data["salary"]["currency"]
    assert vacancy.description == vacancy_data["snippet"]["responsibility"]
    assert vacancy.requirements == vacancy_data["snippet"]["requirement"]

def test_validate_salary(vacancy):
    assert vacancy._Vacancy__validate_salary(100000) == 100000
    assert vacancy._Vacancy__validate_salary(None) == 0
    assert vacancy._Vacancy__validate_salary("abc") == 0

def test_str(vacancy):
    expected_str = (
        "Вакансия: Python Developer\n"
        "Зарплата: 100000-150000 RUR\n"
        "Описание: Разработка на Python...\n"
        "Ссылка: https://hh.ru/vacancy/123456\n"
    )
    assert str(vacancy) == expected_str

def test_cast_to_object_list(vacancy_data):
    vacancies_data = [vacancy_data]
    vacancies = Vacancy.cast_to_object_list(vacancies_data)
    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancy)
    assert vacancies[0].title == "Python Developer"

def test_to_dict(vacancy):
    vacancy_dict = vacancy.to_dict()
    assert vacancy_dict["title"] == "Python Developer"
    assert vacancy_dict["url"] == "https://hh.ru/vacancy/123456"
    assert vacancy_dict["salary"]["from"] == 100000
    assert vacancy_dict["salary"]["to"] == 150000
    assert vacancy_dict["salary"]["currency"] == "RUR"
    assert vacancy_dict["description"] == "Разработка на Python"
    assert vacancy_dict["requirements"] == "Опыт работы с Python"

if __name__ == "__main__":
    pytest.main()