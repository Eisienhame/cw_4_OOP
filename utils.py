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

def getdata_sj():
    '''Загружаем данные с SJ в список'''
    vacan_data = []
    headers = {'X-Api-App-Id': 'v3.r.137072254.91507caae1057df778d94b793caa49bbb3f527c1.e45a120ec40cec1fceb1cd98813e2ff196b99ac7'}
    vacan_data.append(requests.get('https://api.superjob.ru/2.0/vacancies/?page=0&count=1', headers=headers).json())

    return vacan_data
k = getdata_sj()
print(k)
print((k[0]['objects'][0]['payment_from']))  # зп от
print((k[0]['objects'][0]['payment_to']))   # зп до
print((k[0]['objects'][0]['town']['title']))   # адрес работы
print((k[0]['objects'][0]['profession']))   # название вакансии
print((k[0]['objects'][0]['client']['title']))   # название работадателя
print((k[0]['objects'][0]['candidat']))   # описание вакансии
print((k[0]['objects'][0]['work']))   # обязанности вакансии
print((k[0]['objects'][0]['link']))   # ссылка