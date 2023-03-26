import requests, json
from classes import HH, Engine, Superjob, Vacancy

main_exit = True
menu_exit = True

while main_exit is True:
    while menu_exit:
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


            main_exit = False # здесь цикл while меню
            break