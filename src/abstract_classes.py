from abc import ABC, abstractmethod
import requests


class VacancyAPI(ABC):
    """Абстрактный класс для работы с API платформ с вакансиями"""

    @abstractmethod
    def get_vacancies(self, search_query: str) -> list[dict]:
        """Получить вакансии по поисковому запросу"""
        pass


class Saver(ABC):
    """Абстрактный класс для сохранения вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy_data: dict) -> None:
        """Добавить вакансию в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: dict) -> list[dict]:
        """Получить вакансии по критериям"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_data: dict) -> None:
        """Удалить вакансию из файла"""
        pass