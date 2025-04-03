import pytest
from src.api import HeadHunterAPI

@pytest.fixture
def hh_api():
    return HeadHunterAPI()

def test_get_vacancies(hh_api):
    vacancies = hh_api.get_vacancies("Python")
    assert isinstance(vacancies, list)
    assert len(vacancies) > 0
    assert "name" in vacancies[0]