import requests, json
from utils import getdata_hh, getdata_sj
from abc import abstractmethod


class Engine():
    @abstractmethod
    def get_request_hh(self):
        'В зависимости от необходимого сервиса HH/SJ создается  файл с отосортированными ваансиями'
        #getdata_hh()
        work_dic_hh = []
        with open("data_file.json", "r") as write_file:
            dic_hh = json.load(write_file)
            for i in dic_hh:
                for n in range(len(i['items'])):

                    work_dic_hh.append({f"'name': {i['items'][n]['name']}",
                                        f"'url': {i['items'][n]['alternate_url']}",
                                        f"'area': {i['items'][n]['area']['name']}",
                                        f"'salary_from': {i['items'][n]['salary']['from']}",
                                        f"'salary_to': {i['items'][n]['salary']['to']}",
                                        f"'employer': {i['items'][n]['employer']['name']}",
                                        f"'requirement': {i['items'][n]['snippet']['requirement']}", #требоваия
                                        f"'responsibility': {i['items'][n]['snippet']['responsibility']}"})  #описание
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

                    work_dic_sj.append({f"name': {i['objects'][n]['profession']},"
                                        f"'url': {i['objects'][n]['link']},"
                                        f"'area': {i['objects'][n]['town']['title']},"
                                        f"'salary_from': {i['objects'][n]['payment_from']},"
                                        f"'salary_to': {i['objects'][n]['payment_to']},"
                                        f"'employer': {i['objects'][n]['client']['title']},"
                                        f"'requirement': {i['objects'][0]['work']}", #требоваия
                                        f"'responsibility': {i['objects'][0]['candidat']}"})  #описание

                    print(work_dic_sj)

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """

    pass
class Vacancy_hh(Engine):
    ''' Класс для работы и хранения данных о вакансии'''
    def __init__(self):
        self.__name = ''
        self.__url = ''
        self.__area = ''
        self.__salary = ''
        self.__responsibility = ''
        self.__requirement = ''

    def __repr__(self):
        return f'Название вакансии: {self.__name} \n Ссылка на вакансию: {self.__url} \n Город: {self.__area} \n Зарплата: {self.__salary} \n Описание: {self.__responsibility} Требования: {self.__requirement}'