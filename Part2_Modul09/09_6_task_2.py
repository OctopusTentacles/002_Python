# Задача 2. Дзен Пайтона
# Что нужно сделать
# В файле zen.txt хранится так называемый Дзен Пайтона — 
# текст философии программирования на языке Python. Выглядит он так:

# Напишите программу, которая выводит на экран 
# все строки этого файла в обратном порядке.
# Кстати, попробуйте открыть консоль Python и ввести команду import this.

# Результат работы программы:
# Namespaces are one honking great idea -- let's do more of those!
# If the implementation is easy to explain, it may be a good idea.
# If the implementation is hard to explain, it's a bad idea.

import os

def find_dir(cur_path, name_file):
    for i_dir in os.listdir(cur_path):
        find_path = os.path.join(cur_path, i_dir)
        if i_dir == name_file:
            return os.path.abspath(find_path)
        elif os.path.isdir(find_path):
            result = find_dir(find_path, name_file)
            if result:
                return result


path = find_dir('..', 'zen.txt')
# у меня для нахождения пути к файлу или директории
# всегда используется код выше - одна и та же функция.
# это нормально(правильно)???

# в гугле нашел такую штуку:
# dir = os.path.dirname(__file__)
# дает путь в директорию скрипта, 
# но мы такие черточки))))) не проходили, поэтому оставил def

zen_file = open(path, 'r', encoding='utf8')
zen_list = [i_line for i_line in zen_file]
print(*zen_list[::-1])
# * - распаковывает объект в отдельные элементы