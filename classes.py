import requests, json
from utils import getdata_hh, getdata_sj
from abc import abstractmethod


class Engine():
    @abstractmethod
    def get_request_hh(self):
        'В зависимости от необходимого сервиса HH/SJ создается  файл с отосортированными вакансиями'
        #getdata_hh()
        work_dic_hh = []
        with open("data_file.json", "r") as write_file:
            dic_hh = json.load(write_file)
            for i in dic_hh:
                for n in range(len(i['items'])):
                    'Значение зп всместо от и до будет иметь 1 значение, и знач от в приоритете'
                    if i['items'][n]['salary']['from'] is None and i['items'][n]['salary']['to'] is None:
                        salary_single = 'Unknown'
                    elif i['items'][n]['salary']['from'] is None and i['items'][n]['salary']['to'] > 0:
                        salary_single = i['items'][n]['salary']['to']
                    else:
                        salary_single = i['items'][n]['salary']['from']

                    'Если строка требований больше 150 знаков - укоротим'
                    if i['items'][n]['snippet']['requirement'] is None:
                        red_requir = 'No'
                    elif len(i['items'][n]['snippet']['requirement']) > 150:
                        red_requir = i['items'][n]['snippet']['requirement']
                        red_requir = red_requir[:150] + '...'
                    else:
                        red_requir = i['items'][n]['snippet']['requirement']

                    'Если строка описания больше 150 знаков - укоротим'
                    if i['items'][n]['snippet']['responsibility'] is None:
                        red_response = 'No'
                    elif len(i['items'][n]['snippet']['responsibility']) > 150:
                        red_response = i['items'][n]['snippet']['responsibility']
                        red_response = red_response[:150] + '...'
                    else:
                        red_response = i['items'][n]['snippet']['responsibility']



                    work_dic_hh.append({f"'name': {i['items'][n]['name']}",
                                        f"'url': {i['items'][n]['alternate_url']}",
                                        f"'area': {i['items'][n]['area']['name']}",
                                        f"'salary': {salary_single}",
                                        f"'employer': {i['items'][n]['employer']['name']}",
                                        f"'requirement': {red_requir}", #требоваия
                                        f"'responsibility': {red_response}"})  #описание
        return work_dic_hh

    @abstractmethod
    def get_request_sj(self):
        'В зависимости от необходимого сервиса HH/SJ создается  файл с отосортированными ваансиями'
        #getdata_sj()
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
                    elif len(i['objects'][n]['work']) > 150:
                        red_requir = i['objects'][n]['work']
                        red_requir.replace('\n', '')
                        red_requir = red_requir[:150] + '...'
                    else:
                        red_requir = i['objects'][n]['work']
                        red_requir.replace('\n', '')

                    'Если строка описания больше 150 знаков - укоротим'
                    if i['objects'][n]['candidat'] is None:
                        red_response = 'No'
                    elif len(i['objects'][n]['candidat']) > 150:
                        red_response = i['objects'][n]['candidat']
                        red_response.replace('\n', '')
                        red_response = red_response[:150] + '...'
                    else:
                        red_response = i['objects'][n]['candidat']
                        red_response.replace('\n', '')

                    work_dic_sj.append({f"'name': {i['objects'][n]['profession']},"
                                        f"'url': {i['objects'][n]['link']},"
                                        f"'area': {i['objects'][n]['town']['title']},"
                                        f"'salary': {salary_single},"
                                        f"'employer': {i['objects'][n]['client']['title']},"
                                        f"'requirement': {red_requir}", #требоваия
                                        f"'responsibility': {red_response}"})  #описание
                print(work_dic_sj)
        return work_dic_sj


    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
    pass


class HH(Engine):
    def __init__(self, key_search):
        data = self.get_request_hh()

class Superjob(Engine):
    def __init__(self, key_search):
        data = self.get_request_sj()
        search_vac = []

        with open("searching_vac.json", "w", encoding='utf-8') as write_file:
            pass
        with open("searching_vac.json", "w", encoding='utf-8') as write_file:
            json.dump(vacan_data, write_file, indent=4)
class Vacancy_hh():
    ''' Класс для работы и хранения данных о вакансии'''
    def __init__(self, data):
        self.__name = ''
        self.__url = ''
        self.__area = ''
        self.__salary = ''
        self.__responsibility = ''
        self.__requirement = ''

    def __repr__(self):
        return f'Название вакансии: {self.__name} \n Ссылка на вакансию: {self.__url} \n Город: {self.__area} \n Зарплата: {self.__salary} \n Описание: {self.__responsibility} Требования: {self.__requirement}'

