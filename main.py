from src.api import HeadHunterAPI, SuperJobAPI
from src.json_data import JSONSaver


def main():
    vacancies_json = []
    # Получение вакансий по запросу от пользователя
    keyword = input('Введите слово для поиска - ')

    hh_api = HeadHunterAPI(keyword)
    sj_api = SuperJobAPI(keyword)
    for api in (hh_api, sj_api):
        api.get_vacancies(page_count=10)
        vacancies_json.extend(api.get_formatted_vacancies())

    json_data = JSONSaver('python')
    json_data.write_data(vacancies_json)

    while True:
        command = input(
            'Вывести список вакансий - 1,\n'
            'Отсортировать по минимальной зарплате - 2,\n'
            'Для выхода наберите exit.\n'
        )

        if command.lower() == 'exit':
            break
        elif command == '1':
            vacancies = json_data.display_vacancies()
        elif command == '2':
            vacancies = json_data.sorted_by_salary()

        for vacancy in vacancies:
            print(vacancy, end='\n')

if __name__ == "__main__":
    main()







