# Задача 2. Пути файлов
# Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам 
# указанной директории (по умолчанию — корневой диск), находит указанный пользователем 
# каталог и генерирует пути всех встреченных файлов. 
# В решении не нужно использовать рекурсию.

# Подсказка: вместо написания кода с рекурсией используйте готовую 
# рекурсивную функцию os.walk() — os — Miscellaneous operating system interfaces — 
# Python 3.11.0 documentation.


import os

def gen_files_path(folder_name):
    for dirpath, dirnames, filenames in os.walk('/'):

        for filename in filenames:
            yield ("\t\tФайл: ", os.path.join(dirpath, filename))


        for dirname in dirnames:
            if folder_name == dirname:
                yield "\nКаталог: ", os.path.join(dirpath, dirname)
            


            
# /Users/artem/Documents/PROGRAMMING
# /Users/artem/Downloads/Musik
# print(os.listdir('/'))
# print(os.path.abspath('/'))


catalog = gen_files_path(input("Имя каталога: "))
for dir in catalog:
    print(*(dir))
