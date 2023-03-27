import requests, json, re
from utils import getdata_hh, getdata_sj
from abc import abstractmethod


class Engine():
    @abstractmethod
    def get_request_hh(self):
        'В зависимости от необходимого сервиса HH/SJ создается  файл с отосортированными вакансиями'
        getdata_hh()
        work_dic_hh = []
        with open("data_file.json", "r") as write_file:
            dic_hh = json.load(write_file)
            for i in dic_hh:
                for n in range(len(i['items'])):
                    'Значение зп всместо от и до будет иметь 1 значение, и знач от в приоритете'
                    if i['items'][n]['salary'] is None:
                        salary_single = 'Unknown'
                    elif i['items'][n]['salary']['from'] is None and i['items'][n]['salary']['to'] is None:
                        salary_single = 'Unknown'
                    elif i['items'][n]['salary']['from'] is None and i['items'][n]['salary']['to'] > 0:
                        salary_single = i['items'][n]['salary']['to']
                    else:
                        salary_single = i['items'][n]['salary']['from']

                    'Если строка требований больше 150 знаков - укоротим'
                    if i['items'][n]['snippet']['requirement'] is None:
                        red_requir = 'No'
                    elif len(i['items'][n]['snippet']['requirement']) > 200:
                        red_requir = i['items'][n]['snippet']['requirement']
                        red_requir = red_requir[:200] + '...'
                    else:
                        red_requir = i['items'][n]['snippet']['requirement']

                    'Если строка описания больше 150 знаков - укоротим'
                    if i['items'][n]['snippet']['responsibility'] is None:
                        red_response = 'No'
                    elif len(i['items'][n]['snippet']['responsibility']) > 200:
                        red_response = i['items'][n]['snippet']['responsibility']
                        red_response = red_response[:200] + '...'
                    else:
                        red_response = i['items'][n]['snippet']['responsibility']

                    next_item = {'name': i['items'][n]['name'],
                                 'url': i['items'][n]['alternate_url'],
                                 'area': i['items'][n]['area']['name'],
                                 'salary': salary_single,
                                 'employer': i['items'][n]['employer']['name'],
                                 'requirement': red_requir,  # требоваия
                                 'responsibility': red_response}  # описание

                    work_dic_hh.append(next_item)

        return work_dic_hh

    @abstractmethod
    def get_request_sj(self):
        'В зависимости от необходимого сервиса HH/SJ создается  файл с отосортированными вакансиями'
        getdata_sj()
        work_dic_sj = []
        with open("data_file.json", "r") as write_file:
            dic_sj = json.load(write_file)
            for i in dic_sj:
                for n in range(len(i['objects'])):
                    'Значение зп всместо от и до будет иметь 1 значение, и знач от в приоритете'
                    if i['objects'][n]['payment_from'] == 0 and i['objects'][n]['payment_to'] == 0:
                        salary_single = 'Unknown'
                    elif i['objects'][n]['payment_from'] == 0 and i['objects'][n]['payment_to'] > 0:
                        salary_single = i['objects'][n]['payment_to']
                    else:
                        salary_single = i['objects'][n]['payment_from']

                    'Если строка требований больше 150 знаков - укоротим'
                    if i['objects'][n]['work'] is None:
                        red_requir = 'No'
                    elif len(i['objects'][n]['work']) > 200:
                        red_requir = i['objects'][n]['work']
                        red_requir.re.sub('\n', '', red_requir)
                        red_requir = red_requir[:200] + '...'
                    else:
                        red_requir = i['objects'][n]['work']
                        red_requir.re.sub('\n', '', red_requir)

                    'Если строка описания больше 150 знаков - укоротим'
                    if i['objects'][n]['candidat'] is None:
                        red_response = 'No'
                    elif len(i['objects'][n]['candidat']) > 200:
                        red_response = i['objects'][n]['candidat']
                        red_response = re.sub('\n', '', red_response)
                        red_response = red_response[:200] + '...'
                    else:
                        red_response = i['objects'][n]['candidat']
                        red_response = re.sub('\n', '', red_response)

                    'Если не названия работадателя ставим Unknown'
                    if len(i['objects'][n]['client']) < 2:
                        employer_single = 'Unknown'
                    else:
                        employer_single = i['objects'][n]['client']['title']

                    work_dic_sj.append({'name': i['objects'][n]['profession'],
                                        'url': i['objects'][n]['link'],
                                        'area': i['objects'][n]['town']['title'],
                                        'salary': salary_single,
                                        'employer': employer_single,
                                        'requirement': red_requir,  # требоваия
                                        'responsibility': red_response})  # описание
        return work_dic_sj

    @staticmethod
    def get_connector():
        """ Коннект к файлу с вакансиями позьзователя """
        with open("searching_vac.json", "r") as write_file:
            data = json.load(write_file)

        return data

    def see_vacansies(self, n):
        'n - кол-во показывваемых вакансий'
        i = self.get_connector()
        i_count = 0
        for vacan in i:
            s = Vacancy(vacan)
            print(s)
            i_count += 1
            if i_count == n:
                break

    def see_top_10(self):
        'Показывает топ-10 по Зп вакансий из списка пользователя'
        data = self.get_connector()
        best_list = []
        if self.get_len_search_vac() > 10:
            top_count = 10
        else:
            top_count = self.get_len_search_vac()
        for n in range(top_count):
            index = 0
            best_salary = 0
            best_index = 0
            for i in data:
                if i['salary'] == 'Unknown':
                    pass
                else:
                    if int(i['salary']) > best_salary:
                        best_salary = int(i['salary'])
                        best_index = index
                index += 1
            if best_salary != 0:
                best_list.append(data[best_index])
                data.pop(best_index)

        for vacan in best_list:
            s = Vacancy(vacan)
            print(s)

    def find_city(self, search_city:str):
        'Делается выборка вакансий по указанному городу и показывается'
        data = self.get_connector()
        count_city = 0
        for i in data:
            if search_city.lower() in i['area'].lower():
                s = Vacancy(i)
                print(s)
                count_city += 1
        if count_city == 0:
            print('Нет такого города')
    def get_len_search_vac(self):
        'Дает значение кол-ва найденных вакансий'
        i = self.get_connector()
        return len(i)

class HH(Engine):
    '''Формируем класс ХХ по искомому знач в названии вакансии, и создаем файл json с необходимыми параметрами'''

    def __init__(self, key_search):
        data = self.get_request_hh()
        if type(key_search) != str:
            raise TypeError("Некорректный запрос на поиск вакансий")
        else:
            searching_list = []
            for i in data:
                if key_search.lower() in str(i['name']).lower():
                    searching_list.append(i)
            with open("searching_vac.json", "w", encoding='utf-8') as write_file:
                json.dump(searching_list, write_file, indent=4)


class Superjob(Engine):
    '''Формируем класс SJ по искомому знач в названии вакансии, и создаем файл json с необходимыми параметрами'''

    def __init__(self, key_search):
        data = self.get_request_sj()
        if type(key_search) != str:
            raise TypeError("Некорректный запрос на поиск вакансий")
        else:
            searching_list = []
            for i in data:
                if key_search.lower() in str(i['name']).lower():
                    searching_list.append(i)
            with open("searching_vac.json", "w", encoding='utf-8') as write_file:
                json.dump(searching_list, write_file, indent=4)


class Vacancy():
    ''' Класс для работы и хранения данных о вакансии'''

    def __init__(self, data: dict):
        self.__name = data['name']
        self.__url = data['url']
        self.__area = data['area']
        self.__salary = data['salary']
        self.__responsibility = data['responsibility']
        self.__requirement = data['requirement']

    def __repr__(self):
        return f'Название вакансии: {self.__name} \n Ссылка на вакансию: {self.__url} \n Город: {self.__area} \n Зарплата: {self.__salary} \n Описание: {self.__responsibility}\n Требования: {self.__requirement}'

    def __lt__(self, other):
        if type(self.__salary) == str or type(other.__salary) == str:
            raise TypeError("Невозможно сравнить так как у одной из вакансий ЗП неизвестна")
        return self.__salary < other.__salary

    def __gt__(self, other):
        if type(self.__salary) == str or type(other.__salary) == str:
            raise TypeError("Невозможно сравнить так как у одной из вакансий ЗП неизвестна")
        return self.__salary > other.__salary
