from typing import List, Dict


class Vacancy:
    """Класс для представления вакансии"""

    __slots__ = ("title", "url", "salary_from", "salary_to", "currency", "description", "requirements")

    def __init__(self, title: str, url: str, salary: Dict, description: str, requirements: str):
        """Инициализация вакансии с валидацией данных"""
        self.title = str(title) if title else "Без названия"
        self.url = str(url) if url else ""
        self.salary_from = self.__validate_salary(salary.get("from")) if salary else 0
        self.salary_to = self.__validate_salary(salary.get("to")) if salary else 0
        self.currency = str(salary.get("currency")) if salary and salary.get("currency") else "RUR"
        self.description = str(description) if description else ""
        self.requirements = str(requirements) if requirements else ""

    def __validate_salary(self, salary: any) -> int:
        """Валидация зарплаты"""
        if salary is None:
            return 0
        try:
            return int(salary)
        except (ValueError, TypeError):
            return 0

    def __str__(self) -> str:
        return (f"Вакансия: {self.title}\n"
                f"Зарплата: {self.salary_from}-{self.salary_to} {self.currency}\n"
                f"Описание: {self.description[:100]}...\n"
                f"Ссылка: {self.url}\n")

    @classmethod
    def cast_to_object_list(cls, vacancies_data: List[Dict]) -> List['Vacancy']:
        """Преобразовать список словарей в список объектов Vacancy"""
        return [cls(
            title=v.get("name", ""),
            url=v.get("alternate_url", ""),
            salary=v.get("salary"),
            description=v.get("snippet", {}).get("responsibility", ""),
            requirements=v.get("snippet", {}).get("requirement", "")
        ) for v in vacancies_data]

    def to_dict(self) -> dict:
        """Преобразует объект Vacancy в словарь для хранения"""
        return {
            "title": self.title,
            "url": self.url,
            "salary": {
                "from": self.salary_from,
                "to": self.salary_to,
                "currency": self.currency
            },
            "description": self.description,
            "requirements": self.requirements
        }

