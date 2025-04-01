import pytest
from hh_api import HeadHunterAPI


@pytest.fixture
def hh_api():
    return HeadHunterAPI()


def test_get_vacancies(hh_api):
    vacancies = hh_api.get_vacancies("Python", per_page=5)
    assert isinstance(vacancies, list)
    assert len(vacancies) <= 5
    if vacancies:
        assert "name" in vacancies[0]
        assert "salary" in vacancies[0]
        assert "alternate_url" in vacancies[0]