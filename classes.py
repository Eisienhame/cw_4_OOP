import requests, json
from utils import getdata_hh


class Engine():
    @abstractmethod
    def get_request_hh(self):
        'В зависимости от необходимого сервиса HH/SJ создается  файл с отосортированными ваансиями'
        'Файл в json формате будет создан и с него уже будет делать запросы пользователь'
        list_hh = getdata_hh()
        dic_hh = {
            "vacancies": []
        }
        for i in list_hh:
            for n in range(len(i['items'])):
                dic_hh["vacancies"].append({f"name': {i['items'][n]['name']},"
                                            f"'url': {i['items'][n]['alternate_url']},"
                                            f"'area': {i['items'][n]['area']['name']},"
                                            f"'salary_from': {i['items'][n]['salary']['from']},"
                                            f"'salary_to': {i['items'][n]['salary']['to']},"
                                            f"'employer': {i['items'][n]['employer']['name']},"
                                            f"'professional_roles': {i['items'][n]['professional_roles'][0]['name']},"
                                            f"'requirement': {i['items'][n]['snippet']['requirement']},"
                                            f"'responsibility': {i['items'][n]['snippet']['responsibility']}"})
            with open("data_file.json", "w") as write_file:
                pass
            with open("data_file.json", "w") as write_file:
                json.dump(dic_hh, write_file)
    @abstractmethod
    def get_request_sj(self):
        'В зависимости от необходимого сервиса HH/SJ создается  файл с отосортированными ваансиями'
        'Файл в json формате будет создан и с него уже будет делать запросы пользователь'
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """

    pass
