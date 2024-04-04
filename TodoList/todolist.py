from datetime import *
import sys
import os
import time

today = datetime.today().date() #Сегодняшний день
strToday = str(today)+'.txt'

current_file = os.path.realpath(__file__)         #определение местоположения файля для проеверки существования
current_directory = os.path.dirname(current_file)
road_file = f'{current_directory}\\{strToday}' # файл актуального дня

def Checking_the_string():
    os.system('cls')
    try:
        s = input('Введите дату в формате "DD MM": ').split(' ')
        day = int(s[0])
        month =int(s[1])
        return day,month
    except ValueError:
        print('Cтрока не корректна, введите числа')
        time.sleep(1)
        Checking_the_string()

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
    new_data = Checking_the_string()
    try:
        testDay = today.replace(month=new_data[0],day=new_data[1])# день введенный пользователем
        Creating_a_file_name.aDay = testDay
        new_path = str(Creating_a_file_name.aDay)+'.txt'
        new_path= f'{current_directory}\\{new_path}'
        #print(new_path)
        return new_path
    except ValueError:
        print('Пространственно временной континиум нарушен!\nДо взрыва ...')
        for i in range(1,4,):
            print(i)
            time.sleep(1)
        os.system('cls')
        time.sleep(3)
        print('Ха, Наебал!')
        time.sleep(1)
        Creating_a_file()

def Adding_tasks(filename,list_task):
#баг если файл существует но пустой , не получится вписать
    file = open(filename,'a', encoding='UTF-8')
    for task in list_task:
            #print(task)
        file.write(str(task) + '\n')
    file.close()
    #main(road_file,today)

def Creating_a_task_list(filename):
    os.system('cls')
    print('Для завершения нажмите Enter\n')
    if os.path.exists(filename):
        Output_of_tasks(filename,Creating_a_file_name.aDay)
    list_tasks = []
    print()

    print(f'Добавление задач:')
    for n,task in enumerate(sys.stdin,start=1):
        task = task.strip()
        if len(task) > 1:
            list_tasks.append((task,priority_selection()))
            print(f'Задача №{n} добавлена!')
        else:
            break
    return list_tasks

# Вывод задач
def Output_of_tasks(filename=road_file,day=today):
    #os.system('cls')
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
                           
    else:
        print()
        print(f'На {Creating_a_file_name.aDay} задач нет!\n')
        print(f'Добавить задачи на {Creating_a_file_name.aDay}?')
        yn = input('Y/n: ').lower()
        if yn == 'y':
            list_task = Creating_a_task_list(filename)
            Adding_tasks(filename,list_task)
        else:
            menu()
        
def viewing_tasks():# Просмотр задач
    #os.system('cls')
    filename = Creating_a_file_name()
    day = Creating_a_file_name.aDay
    Output_of_tasks(filename,day)

#создание имени и пути файла
def Creating_a_file():
    #os.system('cls')
    filename=Creating_a_file_name()
    list_task = Creating_a_task_list(filename)
    Adding_tasks(filename,list_task)

def menu_2():
    os.system('cls')
    print('1. Добавить задачу на сегодня')
    print('2. Добавить задачу на другой день')
    X = int(input())
    if X == 1:
        list_task = Creating_a_task_list(road_file)
        Adding_tasks(road_file,list_task)
    elif X == 2:
        Creating_a_file()
    else:
        print('Выберите 1 или 2')
        time.sleep(1)
        menu_2()

dictionary_of_modules = {1 :menu_2,2 :viewing_tasks}

def menu():
    print()
    print('1. Добавление задач')
    print('2. Просмотр задач')
    #print('5.Обновить данные')
    print('0. Завершение работы')
    X = int(input(': '))

    if X in dictionary_of_modules:
        dictionary_of_modules[X]()
    elif X == 0:
        exit()

def Task_today():
    if os.path.exists(road_file): # проверка
        Output_of_tasks()
    else:
        print()
        print(f'---  {today}  ---')
        print('На сегодня задач нет!\n')

def main():
    os.system('cls')
    Task_today()
    menu()

main()
while True:
    Task_today()
    menu()