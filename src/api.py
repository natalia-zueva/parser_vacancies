import requests
from abc import ABC, abstractmethod
import json


class ApiClient(ABC):
    """
    Абстрактный класс для получения вакансий с помощью API
    """

    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_vacancies(self, page_count):
        pass


class HeadHunterAPI(ApiClient):
    """
    Класс для работы с API HeadHunter: получает вакансии по запросу пользователя
    """
    url = "https://api.hh.ru/vacancies"

    def __init__(self, keyword):
        self.keyword = keyword
        self.vacancies = []
        self.headers = {"User-Agent": "Vacancies_ParserApp/1.0"}
        self.params = {
            "text": self.keyword,  # Текст поискового запроса
            "area": 1,  # Код региона (1 - Москва)
            "per_page": 100,  # Количество вакансий на странице
            "page": 0,  # Номер страницы
            "currency": "RUR",  # Валюта вакансии
            "archived": False
        }

    def get_request(self):
        response_hh = requests.get(self.url, headers=self.headers, params=self.params)
        data_api_hh = response_hh.json()['items']
        return data_api_hh

    def get_vacancies(self, page_count):
        self.vacancies = []
        for page in range(page_count):
            vacancies_api_page = []
            self.params['page'] = page
            print(f'Обрабатывается {page+1} страница сайта HeadHunter')
            vacancies_api_page = self.get_request()
            self.vacancies.extend(vacancies_api_page)
        return self.vacancies

    def get_formatted_vacancies(self):
        formatted_vacancies = []

        for vacancy in self.vacancies:
            formatted_vacancy = {
                'employer': vacancy['employer']['name'],
                'vacancy': vacancy['name'],
                'url': vacancy['alternate_url'],
                'currency': 'RUR',
                'api': 'Head Hunter'
            }
            salary = vacancy['salary']
            if salary:
                formatted_vacancy['salary_from'] = vacancy['salary']['from']
                formatted_vacancy['salary_to'] = vacancy['salary']['to']
            else:
                formatted_vacancy['salary_from'] = None
                formatted_vacancy['salary_to'] = None
            formatted_vacancies.append(formatted_vacancy)

        return formatted_vacancies


class SuperJobAPI(ApiClient):
    """
    Класс для работы с API SuperJob: получает вакансии по запросу пользователя
    """
    url="https://api.superjob.ru/2.0/vacancies/"

    def __init__(self, keyword):
        self.keyword = keyword
        self.vacancies = []
        self.headers = {
            "X-Api-App-Id": 'v3.r.131353004.e21dd97ef97560b801e7271bf8905da1c7a47507.49f112449b3e8ab49b088918966d1feb87cbac16'
        }
        self.params = {
            "keyword": self.keyword,
            "page": 0,
            "count": 100,
            "is_closed": False,
            "currency": 'rub',
            "town": 4
        }

    def get_request(self):
        response_sj = requests.get(self.url, headers=self.headers, params=self.params)
        data_api_sj = response_sj.json()['objects']
        return data_api_sj

    def get_vacancies(self, page_count):
        self.vacancies = []
        for page in range(page_count):
            vacancies_api_page = []
            self.params['page'] = page
            print(f'Обрабатывается {page+1} страница сайта SuperJob')
            vacancies_api_page = self.get_request()
            self.vacancies.extend(vacancies_api_page)
        return self.vacancies

    def get_formatted_vacancies(self):
        formatted_vacancies = []

        for vacancy in self.vacancies:
            formatted_vacancy = {
                'employer': vacancy['firm_name'],
                'vacancy': vacancy['profession'],
                'salary_from': vacancy['payment_from'] if vacancy['payment_from'] != 0 else None,
                'salary_to': vacancy['payment_to'] if vacancy['payment_to'] != 0 else None,
                'url': vacancy['link'],
                'currency': 'RUR',
                'api': 'Super Job'
            }
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies






