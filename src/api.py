import requests
from typing import List, Dict
from src.abstract import VacancyAPI


class HeadHunterAPI(VacancyAPI):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}

    def __connect(self) -> None:
        """Проверка подключения к API"""
        response = requests.get(self.__base_url, headers=self.__headers)
        response.raise_for_status()

    def get_vacancies(self, search_query: str) -> List[Dict]:
        """Получить вакансии по поисковому запросу"""
        self.__connect()

        params = {
            "text": search_query,
            "per_page": 100,
            "area": 113,  # Россия
            "only_with_salary": True
        }

        response = requests.get(self.__base_url, headers=self.__headers, params=params)
        response.raise_for_status()

        return response.json().get("items", [])