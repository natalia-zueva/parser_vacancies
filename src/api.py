import requests
import json
from abc import ABC, abstractmethod

class API(ABC):
    """
    Абстрактный класс для работы с API
    """

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(API):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, url):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, text: str):
        headers = {"User-Agent": "Vacancies_ParserApp/1.0"}
        params = {
            "text": text.lower(),
            "area": 1
        }
        response_hh = requests.get(self.url, headers=headers, params=params)
        data = response_hh.json()
        return data

hh_api = HeadHunterAPI("https://api.hh.ru/vacancies")
print(hh_api.get_vacancies('python'))


class SuperJobAPI(API):
    """
    Класс для работы с API SuperJob
    """

    def __init__(self, url):
        self.url = "https://api.superjob.ru/2.0/vacancies/"

    def get_vacancies(self, keyword: str):

        headers = {
            "X-Api-App-Id": 'v3.r.131353004.e21dd97ef97560b801e7271bf8905da1c7a47507.49f112449b3e8ab49b088918966d1feb87cbac16'
        }
        params = {
            "keywords": keyword.lower(),
            "town": 4
        }

        response_sj = requests.get(self.url, headers=headers, params=params)
        data = response_sj.json()
        return data

sj_api = SuperJobAPI("https://api.superjob.ru/2.0/vacancies/")
print(sj_api.get_vacancies('python'))
