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
    print('\nПуть:', project)

    if os.path.isfile(project):
        print(f'\tЭто файл '
              f'\n\tРазмер файла: {os.path.getsize(project)} байт')

    elif os.path.isdir(project):
        print('\tЭто папка') 
        print('\tСодержимое каталога:')
        for i_elem in os.listdir(project):
            print('\t',os.path.join(project, i_elem))
         
    else:
        print('\tКаталога не существует')


project_list = ['octopus.jpg', 'Prod', 'Python']
for i_proj in project_list:
    path_project = os.path.abspath(os.path.join('..', i_proj))
    print_dirs(path_project)
