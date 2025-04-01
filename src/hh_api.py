from abstract_classes import VacancyAPI
import requests


class HeadHunterAPI(VacancyAPI):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}

    def __connect(self) -> None:
        """Приватный метод для проверки подключения к API"""
        response = requests.get(self.__base_url, headers=self.__headers)
        response.raise_for_status()

    def get_vacancies(self, search_query: str, per_page: int = 100) -> list[dict]:
        """
        Получить вакансии по поисковому запросу
        :param search_query: Поисковый запрос
        :param per_page: Количество вакансий на странице
        :return: Список вакансий в формате JSON
        """
        self.__connect()
        params = {
            "text": search_query,
            "per_page": per_page,
            "area": 113,  # Россия
            "only_with_salary": True
        }
        response = requests.get(self.__base_url, headers=self.__headers, params=params)
        response.raise_for_status()
        return response.json().get("items", [])