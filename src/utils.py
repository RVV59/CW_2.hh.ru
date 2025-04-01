from typing import List
from vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], filter_words: List[str]) -> List[Vacancy]:
    """Фильтрация вакансий по ключевым словам"""
    if not filter_words:
        return vacancies

    filtered = []
    for vacancy in vacancies:
        description = f"{vacancy.description} {vacancy.requirements}".lower()
        if any(word.lower() in description for word in filter_words):
            filtered.append(vacancy)
    return filtered


def get_vacancies_by_salary(vacancies: List[Vacancy], salary_range: str) -> List[Vacancy]:
    """Фильтрация вакансий по диапазону зарплат"""
    if not salary_range:
        return vacancies

    try:
        min_salary, max_salary = map(int, salary_range.split("-"))
    except ValueError:
        return vacancies

    ranged = []
    for vacancy in vacancies:
        if (vacancy.salary_from >= min_salary and
                (vacancy.salary_to <= max_salary if vacancy.salary_to else True)):
            ranged.append(vacancy)
    return ranged


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортировка вакансий по зарплате (по убыванию)"""
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """Получить топ N вакансий"""
    return vacancies[:top_n]


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """Вывод вакансий в консоль"""
    if not vacancies:
        print("Вакансии не найдены")
        return

    for i, vacancy in enumerate(vacancies, 1):
        print(f"Вакансия #{i}")
        print(vacancy)