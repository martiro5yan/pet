import random
import msvcrt
import time
import os
import sys
from colorama import init, Fore, Back, Style

Stratagems = {
    1: ['⬇', '⬆', '⬆', '⬇', '⬆'],
    2: ['⬇', '⬅', '⬇', '⬆', '⬆', '⬇'],
    3: ['⬇', '⬆', '⬅', '⬆', '⮕', '⮕'],
    4: ['⬇', '⬅', '⬇', '⬇', '⬆', '⬅'],
    5: ['⬇', '⬆', '⬅', '⮕', '⬅', '⮕'],
    6: ['⬇', '⬆', '⬅', '⬆', '⮕', '⬇']
}

def convector(stratagem_arrow):
    stratagem_wasd = []

    for i in stratagem_arrow:
        if i == '⮕':
            stratagem_wasd.append('D')
        elif i == '⬅':
            stratagem_wasd.append('A')
        elif i == '⬇':
            stratagem_wasd.append('S')
        elif i == '⬆':
            stratagem_wasd.append('W')
    return stratagem_wasd

def Withdrawal_of_points_scored(glasses,game_time,blunders):
    init()
    print(f'{menu.username} набрал {Fore.GREEN+str(glasses)} стратОчков',Style.RESET_ALL)
    print()
    print(f'Время игры: {game_time}')
    print(f'Промахи: {blunders}')
    menu()

def The_wrong_character(c): # Вывод НЕправильного символа
    init()
    symbol = ''
    if c == 'D':
        symbol += Fore.RED + '⮕ '
    elif c == 'A':
        symbol += Fore.RED + '⬅ '
    elif c == 'S':
        symbol += Fore.RED + '⬇ '
    elif c == 'W':
        symbol += Fore.RED + '⬆ '
    return symbol+Style.RESET_ALL

def The_corhrect_symbol(c): # Вывод правильного символа
    init()
    symbol = ''
    if c == 'D':
        symbol += Fore.YELLOW + '⮕ '
    elif c == 'A':
        symbol += Fore.YELLOW + '⬅ '
    elif c == 'S':
        symbol += Fore.YELLOW + '⬇ '
    elif c == 'W':
        symbol += Fore.YELLOW + '⬆ '
    return symbol+Style.RESET_ALL


def start():

    start = time.time()  # Получаем текущее время в секундах
    time_limit = 1  # Лимит времени выполнения в секундах

    glasses = 0
    blunders = 0

    while time.time() - start < time_limit:
        key = random.randint(1, 6)
        stratagem_arrow = Stratagems[key]
        stratagem_wasd = convector(stratagem_arrow)
        os.system('cls')
        print(*stratagem_arrow,Style.RESET_ALL)
        for i in stratagem_wasd:
            x = msvcrt.getch().upper().decode('utf-8').upper()
            if x == i:
                print(The_corhrect_symbol(x),end='',flush=True)
                time_limit += 1
                continue
            elif x == 'E':
                menu()
            else:
                print(The_wrong_character(x),end='',flush=True)

                time_limit -= 2
                blunders += 1
                glasses -= 1
        else:
            print()
            glasses += 5
    end = time.time()
    game_time = end - start
    Withdrawal_of_points_scored(glasses,game_time,blunders)

menuDict = {1: start}

def menu():
    #os.system('cls')
    menu.username = input('Введите username: ')
    
    print()
    print('Для набора используйте WASD')
    print('Переключите на ENG расскладку')
    print()

    print('1. Start / Старт')
    choice = int(input(': '))
    if choice == 1:
        menuDict[choice]()
        
menu()
