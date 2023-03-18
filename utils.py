import requests, json


def getdata_hh():
    '''Загружаем данные с ХХ в словарик'''
    vacan_data = []



    for n in range(1, 10):
        params = {
            'area': 113,  # Поиск в Ru зоне
            'page': n,    # Номер страницы
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        vacan_data.append(requests.get('https://api.hh.ru/vacancies', params).json())
    return vacan_data

print(getdata_hh())


