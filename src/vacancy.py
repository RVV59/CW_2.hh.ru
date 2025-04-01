from typing import Any


class Vacancy:
    """Класс для представления вакансии"""

    __slots__ = ("title", "url", "salary_from", "salary_to", "currency", "description", "requirements")

    def __init__(self, title: str, url: str, salary: dict, description: str, requirements: str):
        """
        Инициализация вакансии
        :param title: Название вакансии
        :param url: Ссылка на вакансию
        :param salary: Информация о зарплате
        :param description: Описание вакансии
        :param requirements: Требования к кандидату
        """
        self.title = title
        self.url = url
        self.salary_from = self.__validate_salary(salary.get("from")) if salary else 0
        self.salary_to = self.__validate_salary(salary.get("to")) if salary else 0
        self.currency = salary.get("currency") if salary else "Не указана"
        self.description = description
        self.requirements = requirements

    def __validate_salary(self, salary: Any) -> int:
        """Приватный метод для валидации зарплаты"""
        if salary is None:
            return 0
        try:
            return int(salary)
        except (ValueError, TypeError):
            return 0

    def __str__(self) -> str:
        return (f"Вакансия: {self.title}\n"
                f"Зарплата: {self.salary_from} - {self.salary_to} {self.currency}\n"
                f"Описание: {self.description[:100]}...\n"
                f"Требования: {self.requirements[:100]}...\n"
                f"Ссылка: {self.url}\n")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            return False
        return self.salary_from == other.salary_from and self.salary_to == other.salary_to

    def __lt__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from < other.salary_from

    def __gt__(self, other) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from > other.salary_from

    @classmethod
    def cast_to_object_list(cls, vacancies_data: list[dict]) -> list['Vacancy']:
        """Преобразовать список словарей в список объектов Vacancy"""
        vacancies = []
        for vacancy_data in vacancies_data:
            try:
                vacancy = cls(
                    title=vacancy_data.get("name", ""),
                    url=vacancy_data.get("alternate_url", ""),
                    salary=vacancy_data.get("salary"),
                    description=vacancy_data.get("snippet", {}).get("responsibility", ""),
                    requirements=vacancy_data.get("snippet", {}).get("requirement", "")
                )
                vacancies.append(vacancy)
            except Exception as e:
                print(f"Ошибка при создании вакансии: {e}")
        return vacancies