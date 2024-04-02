from datetime import *
import sys
import os
import time

today = datetime.today().date() #Сегодняшний день
strToday = str(today)+'.txt'

current_file = os.path.realpath(__file__)         #определение местоположения файля для проеверки существования
current_directory = os.path.dirname(current_file)
road_file = f'{current_directory}\\{strToday}'


def list_tuple(Ltuple):
    result = []
    for t in Ltuple:
        t = eval(t)
        result.append(t)
    return result

def priority_selection():
    try:
        priority = int(input('Приоритет задачи от 1 до ..: '))
        if type(priority) == int:
            return priority
    except ValueError:
        print('Введите число')
        for i in range(1,4):
            print(i)
            time.sleep(1)
        priority_selection()

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
            os.system('cls')
        Creating_a_file_name()

def Adding_tasks(filename,list_task):
    if os.path.exists(filename):
        Output_of_tasks(filename,Creating_a_file_name.aDay)#баг если файл существует но пустой , не получится вписать
    file = open(filename,'a', encoding='UTF-8')
    for task in list_task:
            #print(task)
        file.write(str(task) + '\n')
    file.close()
    main(road_file,today)

def Creating_a_task_list():
    list_tasks = []
    print(f'Добавление задач на {Creating_a_file_name.aDay}')
    for task in sys.stdin:
        task = task.strip()
        if len(task) > 1:
            list_tasks.append((task,priority_selection()))
        else:
            break
    return list_tasks

# Вывод задач
def Output_of_tasks(filename=road_file,day=today):
    os.system('cls')
    if os.path.exists(filename):#Вывод задач, по умолчанию актуальный день
        with open(filename, 'r', encoding='UTF-8') as file:
                tasks_list = file.readlines()
                tasks_list = list_tuple(tasks_list)
                sort_list = sorted(tasks_list,reverse=False, key=lambda x: x[1])
                if len(sort_list) == 0:
                    #print(f'---  {day}  ---')
                    print(f'На {day} задач нет!\n')
                else:
                    print(f'---  {day}  ---\n')
                    for task in sort_list:
                        priority = task[1]
                        task = task[0]
                        print(f'-{priority}- {task}')
                    
        #main(road_file,today)        
    else:
        print()
        print(f'На {Creating_a_file_name.aDay} задач нет!')
        print(f'Добавить задачи на {Creating_a_file_name.aDay}?')
        yn = input('Y/n: ').lower()
        if yn == 'y':
            list_task = Creating_a_task_list()
            Adding_tasks(filename,list_task)
        else:
            main(road_file,today)
        
def viewing_tasks():# Просмотр задач
    #os.system('cls')
    filename = Creating_a_file_name()
    day = Creating_a_file_name.aDay
    Output_of_tasks(filename,day)

#создание имени и пути файла
def Creating_a_file():
    #os.system('cls')
    filename=Creating_a_file_name()
    list_task = Creating_a_task_list()
    Adding_tasks(filename,list_task)
    main(road_file,today)

dictionary_of_modules = {1 :Creating_a_file,2 :viewing_tasks}

def main(road_file,today):
    #os.system('cls')

    if os.path.exists(road_file ): # проверка
        Output_of_tasks()
    else:
        print()
        print(f'---  {today}  ---')
        print('На сегодня задач нет!\n')

    print('1.Добавление задач')
    print('2.Просмотр задач')
    #print('5.Обновить данные')
    print('0.Завершение работы')
    X = int(input(': '))

    if X in dictionary_of_modules:
        dictionary_of_modules[X]()
    else:
        exit

main(road_file,today)
while True:
    X = input('Завершить работу? Y/n: ').lower()
    if X == 'y':
        break
    else:
        main(road_file,today)