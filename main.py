import requests, json, re
from utils import getdata_hh, getdata_sj
from classes import HH, Engine, Superjob, Vacancy, Connector

main_exit = True  # ключи для более наглядного завершения программы
menu_exit = True

while main_exit is True:
    while menu_exit is True:
        print('Напишите с какого сайта вы бы хотели искать работу: 1 = "Headhunter", 2 = "Superjob"')
        which_site = input()
        if which_site != '1' and which_site != '2':
            print('Такого варианта нет, выберете другой пожалуйста')
            break
        else:
            print('Напишите название вакансии которую ищите')
            search_vac = input()
            if which_site == '1':
                job_class = HH(search_vac)
            else:
                job_class = Superjob(search_vac)
            vacancy_count = job_class.get_len_search_vac()
            if vacancy_count < 1:
                print('Такой вакансии не найдено, поищите другую')
                break
            else:
                while True:
                    print(f'Найдено {vacancy_count} вакансий. Выберете номер варианта действий:')
                    print('1 - показать необходимое кол-во этих вакансий')
                    print('2 - показать ТОП-10 вакансий по зарплате')
                    print('3 - показать все вакансии в указанном городе')
                    print('0 - для выхода из программы')
                    option_menu = input()
                    if option_menu not in ['1', '2', '3', '0']:
                        print('Некорректный вариант действий, выберете корректный!')
                        continue
                    if option_menu == '1':
                        print(f'Ввиде кол-во для показа. Максимум : {vacancy_count}')
                        which_see = input()
                        if which_see.isdigit() and int(which_see) <= vacancy_count:
                            job_class.see_vacansies(which_see)
                        else:
                            print('Неверное значение')
                            continue

                    if option_menu == '2':
                        job_class.see_top_10()

                    if option_menu == '3':
                        print('Введите название города для поиска')
                        search_city = input()
                        print()
                        job_class.find_city(search_city)

                    if option_menu == '0':
                        print('Спасибо...')
                        main_exit = False
                        menu_exit = False
                        break
