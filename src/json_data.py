import json
# from vacancy import Vacancy

class JSONSaver:
    """
    Класс, записывающий данные в json-файл и выводящий эти данные, а также имеющий метод по сортировке по зарплате
    """

    def __init__(self, keyword):
        self.file = f'{keyword}.json'

    def write_data(self, vacancies_json):
        with open(self.file, 'w', encoding='UTF-8') as file:
            json.dump(vacancies_json, file, indent=4, ensure_ascii=False)

    def display_vacancies(self):
        with open(self.file, 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
        return [Vacancy(x) for x in vacancies]

    def sorted_by_salary(self):
        desc = True if input(
            '< - по увеличению \n'
            '> - по уменьшению \n'
        ).lower() == '>' else False
        vacancies = self.display_vacancies()
        return sorted(vacancies, key=lambda x: [x.salary_from if x.salary_from else 0, x.salary_to if x.salary_to else 0], reverse=desc)


class Vacancy:
    """
    Класс, формирующий экземпляр вакансии
    """

    def __init__(self, vacancy):
        """
        Создание экземпляра класса Vacancy.
        """
        self.employer = vacancy['employer']
        self.name = vacancy['vacancy']
        self.salary_from = vacancy['salary_from']
        self.salary_to = vacancy['salary_to']
        self.currency = vacancy['currency']
        self.url = vacancy['url']

    def __str__(self):
        if not self.salary_from and not self.salary_to:
            salary = f'Не указана'
        else:
            salary_from, salary_to = '', ''
            if self.salary_from:
                salary_from += f'От {self.salary_from} {self.currency}'
            if self.salary_to:
                salary_to += f' до {self.salary_to} {self.currency}'
            salary = ''.join([salary_from, salary_to])
        return f"""
Вакансия: {self.name},
Зарплата: {salary},
Компания: {self.employer}
Ссылка на вакансию: {self.url}
"""

    def __ge__(self, other):
        return self.salary_from >= other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from



