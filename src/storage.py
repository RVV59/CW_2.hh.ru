import json
import os
from typing import List, Dict, Union
# from src.abstract import VacancyAPI
from src.vacancy import Vacancy


class JSONSaver:
    def __init__(self, filename: str = "data/vacancies.json"):
        self.__filename = filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                json.dump([], f)

    def __load_vacancies(self) -> List[Dict]:
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def __save_vacancies(self, vacancies: List[Dict]) -> None:
        """Сохраняет вакансии в файл"""
        with open(self.__filename, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=2)

    def add_vacancy(self, vacancy_data: Union[Dict, Vacancy]) -> None:
        """Добавляет вакансию в хранилище"""
        if isinstance(vacancy_data, Vacancy):
            vacancy_data = vacancy_data.to_dict()

        vacancies = self.__load_vacancies()

        # Проверяем, существует ли уже такая вакансия
        if not any(v.get('url') == vacancy_data.get('url') for v in vacancies):
            vacancies.append(vacancy_data)
            self.__save_vacancies(vacancies)

    def get_vacancies(self, criteria: Dict = None) -> List[Dict]:
        """Возвращает вакансии, соответствующие критериям"""
        vacancies = self.__load_vacancies()
        if not criteria:
            return vacancies

        return [v for v in vacancies if all(
            str(value).lower() in str(v.get(key, '')).lower()
            for key, value in criteria.items()
        )]

    def delete_vacancy(self, vacancy: Union[Dict, Vacancy]) -> None:
        """Удаляет вакансию из хранилища"""
        if isinstance(vacancy, Vacancy):
            vacancy = vacancy.to_dict()

        vacancies = self.__load_vacancies()
        vacancies = [v for v in vacancies if v.get('url') != vacancy.get('url')]
        self.__save_vacancies(vacancies)