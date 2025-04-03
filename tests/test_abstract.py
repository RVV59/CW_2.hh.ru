import pytest

from src.abstract import VacancyAPI

def test_vacancy_api():
    class TestAPI(VacancyAPI):
        def get_vacancies(self, search_query: str) -> list:
            return []

    api = TestAPI()
    vacancies = api.get_vacancies("Python")
    assert isinstance(vacancies, list)