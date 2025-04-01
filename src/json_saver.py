import json
from pathlib import Path
from typing import List, Dict, Any
from abstract_classes import Saver


class JSONSaver(Saver):
    """Класс для сохранения вакансий в JSON-файл"""

    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename
        self.__ensure_file_exists()

    def __ensure_file_exists(self) -> None:
        """Приватный метод для создания файла, если он не существует"""
        Path(self.__filename).touch(exist_ok=True)

    def add_vacancy(self, vacancy_data: Dict[str, Any]) -> None:
        """Добавить вакансию в файл"""
        vacancies = self.get_vacancies({})

        # Проверка на дубликаты по URL
        if any(v.get("url") == vacancy_data.get("url") for v in vacancies):
            return

        vacancies.append(vacancy_data)
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=2)

    def get_vacancies(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Получить вакансии по критериям"""
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                vacancies = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            vacancies = []

        if not criteria:
            return vacancies

        filtered_vacancies = []
        for vacancy in vacancies:
            match = True
            for key, value in criteria.items():
                if key not in vacancy or value.lower() not in str(vacancy[key]).lower():
                    match = False
                    break
            if match:
                filtered_vacancies.append(vacancy)

        return filtered_vacancies

    def delete_vacancy(self, vacancy_data: Dict[str, Any]) -> None:
        """Удалить вакансию из файла"""
        vacancies = self.get_vacancies({})
        vacancies = [v for v in vacancies if v.get("url") != vacancy_data.get("url")]
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=2)