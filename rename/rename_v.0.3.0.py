import os
import time
print('rename v0.3.0\n')

def File_path_input() -> str:
    while True:
        print()
        file_path = input('Введите путь к файлам: ')
        if os.path.isdir(file_path):
            return file_path
        else:
            print('Путь не найден!')

def New_file_names_input() -> str:
    banned = '\\//:*?"<>|' #Запрещенные символы
    while True:
        print()
        new_file_names = input("Введите новое имя файла: ")
        if any(char in banned for char in new_file_names): #Проерка есть ли запрещенные символы
            print('Введены запрещенные символы: \\ // : * ? " < > | ')
        else:
            return new_file_names       

def File_rename_process(new_file_name: str ,file_path: str, filename: str):

    old_file_path = os.path.join(file_path, filename)
    new_file_path = os.path.join(file_path, new_file_name)
    os.rename(old_file_path, new_file_path)

    time.sleep(0.1)
    print("{:<25} ----> {:>5}".format(filename, new_file_name))

def File_naming_process(file_list: list, file_path: str, new_names: str, store_name: str):
    
    file_count = 0
    for filename in file_list:
        if filename[-3:] == 'jpg' or filename[-3:] == 'psd':
            file_format = filename[-3:]
            if store_name == 'DM' or store_name == 'BP':
                if file_format == 'jpg':
                    name = filename[6:]
                    indx = name.find(' ')
                    new_file_name = f'{new_names}_{name[:indx]}_{store_name}.{file_format}'
                    File_rename_process(new_file_name,file_path,filename)
            else:
                indx = name.find(' ')
                new_file_name = f'{new_names}_{name[:indx]}.{file_format}'
                File_rename_process(new_file_name,file_path,filename)
        file_count += 1
    print()
    print(f'Переименовывано {file_count} файлов')

def main():
    
    file_path = File_path_input()
    file_list = os.listdir(file_path)
    new_names = New_file_names_input()
    store_name = file_path[-2:]

    File_naming_process(file_list,file_path,new_names,store_name)

while True:
    main()