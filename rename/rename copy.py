from datetime import *
import time
import os
print('rename v0.2')
print()

def checking_the_file_name():
    banned = '\/:*?"<>|' #Запрещенные символы
    filename = input("Введите имя файла: ")
    if any(char in banned for char in filename): #Проерка есть ли запрещенные символы
        print('Введены запрещенные символы: \ / : * ? " < > | ')
        checking_the_file_name()
    else:
        return(filename)
        
#Функция переименовывание файлов
def rename_file(new_file_name,directory_path,file): 
    old_file_path = os.path.join(directory_path, file)
    new_file_path = os.path.join(directory_path, new_file_name)
    os.rename(old_file_path, new_file_path)
    time.sleep(0.1)
    print(f'{file} ----> {new_file_name}')


def main():

    directory_path = input("Введите путь к файлам: ")

    new_name = checking_the_file_name()
        
    st = '_ _ '
    print(st * 20 + '\n')
    shop = directory_path[-2:] # вычленение имени магазина
    count = 0
    for file in os.listdir(directory_path):
        if file[-3:] == 'jpg':
            count += 1
            # Создаем новое имя файла с учетом номера
            if shop == 'DM' or shop == 'BP': # Проверка магазина и создание нового имени файла
                minus_6 = file[6:]
                ind = (minus_6.find(' '))
                new_file_name = f'{new_name}_{minus_6[:ind]}_{shop}.jpg'
                rename_file(new_file_name,directory_path,file)
            else:           # Создание нового имени файла без привязки к магазину
                ind = (file.find(' '))
                new_file_name = f'{new_name}_{file[:ind]}.jpg'
                rename_file(new_file_name,directory_path,file)
                
    print(st * 20+'\n')            
    print(f'Переименовано {count} файлов.\n')
        
main()