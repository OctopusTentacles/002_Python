# Задача 3. Количество строк
# Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории 
# и вычисляет количество строк в каждом файле, игнорируя пустые строки и строки 
# комментариев. По итогу функция-генератор должна с помощью yield каждый раз 
# возвращать количество строк в очередном файле.


import os



def find_dir(folder_name):
    for dirpath, dirnames, filenames in os.walk('/'):
        for dirname in dirnames:
            if folder_name == dirname:
                return os.path.join(dirpath, dirname)
                





def py_files(cur_dir, ending='.py'):

    for dirpath, dirnames, filenames in os.walk(cur_dir):
        pass


catalog = find_dir(input("Имя каталога: "))
print(catalog)



# /Users/artem/Documents/PROGRAMMING/SkillBox/002_Python/Part2_Modul10/10_6_task_3