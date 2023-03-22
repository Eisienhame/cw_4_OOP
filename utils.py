import requests, json


def getdata_hh():
    '''Загружаем данные с ХХ в список'''
    vacan_data = []

    # for n in range(1, 10):
    #     params = {
    #         'area': 113,  # Поиск в Ru зоне
    #         'page': n,    # Номер страницы
    #         'per_page': 100  # Кол-во вакансий на 1 странице
    #     }
    #     vacan_data.append(requests.get('https://api.hh.ru/vacancies', params).json())
    params = {
        'area': 113,  # Поиск в Ru зоне
        'page': 1,  # Номер страницы
        'per_page': 10  # Кол-во вакансий на 1 странице
    }
    vacan_data.append(requests.get('https://api.hh.ru/vacancies', params).json())
    #print(requests.get('https://api.hh.ru/vacancies')) # <Response [200]>
    return vacan_data
print(getdata_hh())
for i in getdata_hh():
    print(len(i['items']))
    print(i['items'][1]['name'])  #Назавние вакасии
    print(i['items'][1]['area']['name'])  #город
    print(i['items'][1]['salary']['from'])  #зп от
    print(i['items'][1]['salary']['to'])  # зп до
    print(i['items'][1]['alternate_url'])  # ссылка на вакансию
    print(i['items'][1]['employer']['name'])  #Назавние работадателя  9
    print(i['items'][1]['snippet']['requirement'])  # описание вакансии
    print(i['items'][1]['snippet']['responsibility'])  # обязанности
    print(i['items'][1]['professional_roles'][0]['name'])  # роль