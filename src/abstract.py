from abc import ABC, abstractmethod
from typing import List, Dict


class VacancyAPI(ABC):
    """Абстрактный класс для работы с API вакансий"""

    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[Dict]:
        """Получить вакансии по поисковому запросу"""
        pass


class StorageABC(ABC):
    """Абстрактный базовый класс для работы с хранилищем вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy: Dict) -> None:
        """Добавить вакансию в хранилище"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Dict = None) -> List[Dict]:
        """Получить вакансии по критериям"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Dict) -> None:
        """Удалить вакансию из хранилища"""
        pass