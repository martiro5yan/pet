from datetime import *
import sys
import os
import time

today = datetime.today().date() #Сегодняшний день
strToday = str(today)+'.txt'

current_file = os.path.realpath(__file__)           #определение местоположения файля для проеверки существования
current_directory = os.path.dirname(current_file)
road_file = f'{current_directory}\\{strToday}'

def Creating_a_file_name():
    os.system('cls')
    s = input('Введите дату в формате "DD MM": ').split(' ')
    day = int(s[0])
    month =int(s[1])
    try:
        testDay = today.replace(month=month,day=day)# день введенный пользователем
        Creating_a_file_name.aDay = testDay
        new_path = str(Creating_a_file_name.aDay)+'.txt'
        new_path= f'{current_directory}\\{new_path}'
        #print(new_path)
        return new_path
    except ValueError:
        print('Введена некорректная дата.')
        for i in range(1,4):
            print(i)
            time.sleep(1)
        Creating_a_file_name()

def Adding_tasks(filename):
    if os.path.exists(filename):
        Output_of_tasks(filename,Creating_a_file_name.aDay)#баг если файл существует но пустой , не получится вписать
    with open(filename,'a', encoding='UTF-8') as file:
        print(f'Добавление задач на {Creating_a_file_name.aDay}')
        for task in sys.stdin:
            if task != '\n':
                file.write(task)   
            else:
                break
        main(road_file,today)

def Output_of_tasks(filename=road_file,day=today):
    #os.system('cls')
    if os.path.exists(filename):#Вывод задач, по умолчанию актуальный день
        with open(filename, 'r', encoding='UTF-8') as file:
                tasks_list = file.readlines()
                if len(tasks_list) == 0:
                    #print(f'---  {day}  ---')
                    print(f'На {day} задач нет!\n')
                else:
                    print(f'---  {day}  ---\n')
                    for number,task in enumerate(tasks_list,start=1):
                        print(f'-{number}- {task}')
        #main(road_file,today)        
    else:
        print(f'На {Creating_a_file_name.aDay} задач нет!')
        print(f'Добавить задачи на {Creating_a_file_name.aDay}?')
        yn = input('Y/n: ').lower()
        if yn == 'y':
            Adding_tasks(filename)
        else:
            main(road_file,today)
        
def viewing_tasks():# Просмотр задач
    os.system('cls')
    filename = Creating_a_file_name()
    day = Creating_a_file_name.aDay
    Output_of_tasks(filename,day)

def Creating_a_file():
    #os.system('cls')
    filename=Creating_a_file_name()
    Adding_tasks(filename)
    main(road_file,today)

dictionary_of_modules = {1 :Creating_a_file,2 :viewing_tasks}

def main(road_file,today):
    #os.system('cls')

    if os.path.exists(road_file ): # проверка
        Output_of_tasks()
    else:
        print(f'---  {today}  ---')
        print('На сегодня задач нет!\n')

    print('1.Добавление задач')
    print('2.Просмотр задач')
    print('0.Завершение работы')
    X = int(input(': '))

    if X in dictionary_of_modules:
        dictionary_of_modules[X]()
    else:
        main()

main(road_file,today)
while True:
    X = input('Продолжить работу? Y/n: ').lower()
    if X == 'y':
        main(road_file,today)
    else:
        break