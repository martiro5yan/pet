from datetime import *
import time
import os

print('rename v0.2')
print()
# Проверка директории 
def checking_the_listdir():
    road_directory = input('Введите путь к файлам: ')
    if os.path.isdir(road_directory):
        print(*os.listdir(road_directory),sep='\n')
        # yn = input('Переименовать файлы ? (Y/N): ')
        # if yn == 'Y':
        return road_directory
        # else:
        #     checking_the_listdir()
    else:
        print('Путь не найден')
        checking_the_listdir()
# Проверка корректонсти имени файла
def checking_the_file_name():
    banned = '\\//:*?"<>|' #Запрещенные символы
    filename = input("Введите новое имя файла: ")
    if any(char in banned for char in filename): #Проерка есть ли запрещенные символы
        print('Введены запрещенные символы: \\ // : * ? " < > | ')
        checking_the_file_name()
    else:
        return filename


#Функция переименовывания файлов
def rename_file(new_file_name,directory_path,file): 
    old_file_path = os.path.join(directory_path, file)
    new_file_path = os.path.join(directory_path, new_file_name)
    os.rename(old_file_path, new_file_path)
    
    time.sleep(0.1)
    print("{:<25} ----> {:>5}".format(file, new_file_name))


def main():
    while True:
        directory_path = checking_the_listdir()
        print(directory_path)

        new_name = checking_the_file_name()
            
        st = '_ _ '
        print(st * 20 + '\n')
        shop = directory_path[-2:] # вычленение имени магазина
        count = 0
        for file in os.listdir(directory_path):
            if file[-3:] == 'jpg' or file[-3:] == 'psd':
                file_format = file[-3:]
                count += 1
                # Создаем новое имя файла с учетом номера
                if shop == 'DM' or shop == 'BP':
                    if file[-3:] == 'jpg':
                        file_format = file[-3:] # Проверка магазина и создание нового имени файла
                        minus_6 = file[6:]
                        ind = minus_6.find(' ')
                        new_file_name = f'{new_name}_{minus_6[:ind]}_{shop}.{file_format}'
                        rename_file(new_file_name,directory_path,file)
                else:           # Создание нового имени файла без привязки к магазину
                    ind = (file.find(' '))
                    new_file_name = f'{new_name}_{file[:ind]}.{file_format}'
                    rename_file(new_file_name,directory_path,file)
                    
        print(st * 20+'\n')            
        print(f'Переименовано {count} файлов.\n')
            
main()