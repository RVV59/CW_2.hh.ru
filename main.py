from hh_api import HeadHunterAPI
from vacancy import Vacancy
from json_saver import JSONSaver
from utils import (filter_vacancies, get_vacancies_by_salary,
                   sort_vacancies, get_top_vacancies, print_vacancies)


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    print("Добро пожаловать в программу поиска вакансий!")

    # Получение данных от пользователя
    search_query = input("Введите поисковый запрос (например, Python): ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий (через пробел): ").split()
    salary_range = input("Введите диапазон зарплат (например, 100000-150000): ")

    # Получение вакансий с hh.ru
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Сохранение вакансий в файл
    json_saver = JSONSaver()
    for vacancy in vacancies_list:
        json_saver.add_vacancy({
            "title": vacancy.title,
            "url": vacancy.url,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "currency": vacancy.currency,
            "description": vacancy.description,
            "requirements": vacancy.requirements
        })

    # Фильтрация и сортировка вакансий
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # Вывод результатов
    print("\nРезультаты поиска:")
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()