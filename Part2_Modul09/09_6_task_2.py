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

open('zen.txt', 'r', encoding='utf8')