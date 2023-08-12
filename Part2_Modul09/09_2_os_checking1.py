# Задача 1. Иконки
# Андрей для себя хочет сделать экспериментальный сайт, 
# где будет красиво отображаться вся структура его диска: папки одними 
# иконками, файлы — другими. Поэтому ему нужен код, который поможет определить, 
# какой тип иконки вставить.

# Напишите программу, которая по заданному абсолютному пути определяет, 
# на что указывает этот путь (на директорию, файл, или же путь является ссылкой), 
# и выведите соответствующее сообщение. Если путь указывает на файл, 
# то также выведите его размер (сколько он весит в байтах). 
# Обеспечьте контроль ввода: проверка пути на существование. 

# Подсказка: для вывода размера файла поищите соответствующий метод.
# Пример 1:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Это файл
# Размер файла: 605 байт

# Пример 2:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Указанного пути не существует

import os

def print_dirs(project):
    print('Путь:', project)

    if os.path.isfile(project):
        print('    Это файл')
        print('    Размер файла:', os.path.getsize(project))

    elif os.path.exists(project):
        for i_elem in os.listdir(project):
            path = os.path.join(project, i_elem)     
            print(' ', path)   

    else:
        print(' ', 'Каталога не существует')


project_list = ['octopus', 'Prod', 'Python']
for i_proj in project_list:
    path_project = os.path.abspath(os.path.join('..', i_proj))
    print_dirs(path_project)
