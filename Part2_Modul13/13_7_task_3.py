# Задача 3. Количество строк
# Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории 
# и вычисляет количество строк в каждом файле, игнорируя пустые строки и строки 
# комментариев. По итогу функция-генератор должна с помощью yield каждый раз 
# возвращать количество строк в очередном файле.


import os


def py_files(folder_name, ending='.py'):
    
    for dirpath, dirnames, filenames in os.walk('/'):
        for dirname in dirnames:
            if folder_name == dirname:
                my_dir = os.path.join(dirpath, dirname)
                yield "Каталог:", my_dir

                for py_file in os.listdir(my_dir):
                    if py_file.endswith(ending):
                        yield "\tфайл: ", py_file

                        amt_lines = 0
                        with open(os.path.join(my_dir, py_file), 'r', encoding='utf8') as file:
                            for line in file:
                                amt_lines += 1
                            yield "\t\tстрок кода: ", amt_lines

                return



catalog = py_files(input("Имя каталога: "))
for py_file in catalog:
    print(*py_file)


# /Users/artem/Documents/PROGRAMMING/SkillBox/002_Python/Part2_Modul10/10_6_task_3  2
# /Users/artem/Documents/PROGRAMMING/SkillBox/002_Python/Part2_Modul12/12_7_task_4  4