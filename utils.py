import requests, json


def getdata_hh():
    '''Загружаем данные с ХХ в список'''
    vacan_data = []

    for n in range(1, 10):
        params = {
            'area': 113,  # Поиск в Ru зоне
            'page': n,    # Номер страницы
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        vacan_data.append(requests.get('https://api.hh.ru/vacancies', params).json())
    # params = {
    #     'area': 113,  # Поиск в Ru зоне
    #     'page': 1,  # Номер страницы
    #     'per_page': 30  # Кол-во вакансий на 1 странице
    # }
    # vacan_data.append(requests.get('https://api.hh.ru/vacancies', params).json())
    #print(requests.get('https://api.hh.ru/vacancies')) # <Response [200]>
    with open("data_file.json", "w", encoding='utf-8') as write_file:
        pass
    with open("data_file.json", "w", encoding='utf-8') as write_file:
        json.dump(vacan_data, write_file, indent=4)

def getdata_sj():
    '''Загружаем данные с SJ в список'''
    vacan_data = []
    for i in range(10):
        headers = {'X-Api-App-Id': 'v3.r.137072254.91507caae1057df778d94b793caa49bbb3f527c1.e45a120ec40cec1fceb1cd98813e2ff196b99ac7'}
        vacan_data.append(requests.get(f'https://api.superjob.ru/2.0/vacancies/?page={i}&count=100', headers=headers).json())
    with open("data_file.json", "w", encoding='utf-8') as write_file:
        pass
    with open("data_file.json", "w", encoding='utf-8') as write_file:
        json.dump(vacan_data, write_file, indent=4)

