from datetime import *
import time
import os
print('rename v0.1')
print()

def rename_file(new_file_name,directory_path,file):
    old_file_path = os.path.join(directory_path, file)
    new_file_path = os.path.join(directory_path, new_file_name)
    os.rename(old_file_path, new_file_path)
    print(f'{file} ----> {new_file_name}')

while True:
    directory_path = input("Введите путь к файлам: ")
    new_name = input('Введите новое имя: ')
    
    st = '_ _ '
    print(st * 20 + '\n')
    shop = directory_path[-2:]
    count = 0
    for file in os.listdir(directory_path):
        if file[-3:] == 'psd':
            count += 1
                    # Создаем новое имя файла с учетом номера
            if shop == 'DM' or shop == 'BP':
                minus_6 = file[6:]
                ind = (minus_6.find(' '))
                new_file_name = f'{new_name}_{minus_6[:ind]}_{shop}.psd'
                rename_file(new_file_name,directory_path,file)
            else:
                ind = (file.find(' '))
                new_file_name = f'{new_name}_{file[:ind]}.psd'
                rename_file(new_file_name,directory_path,file)
                time.sleep(0.1)
    print(st * 20+'\n')            
    print(f'Переименовано {count} файлов.\n')
    
