# Задача 2. Однострочный код 2
# Пользователь вводит строку, состоящую из любых символов. Напишите код, 
# который выводит на экран список этих символов, 
# исключая цифры и буквы в верхнем регистре.

# Пример работы консоли:
# Введите строку: qWe456rtY

# ['q', 'e', 'r', 't']


# from typing import List

# this_str = input("Введите строку: ")
# если элемент в строке (lambda elem -> for elem in str) является
# например буквой, то фильтруем его (вносим в список).
# нужно исключить -> внести только маленькие буквы

# list_str = list(filter(lambda elem: elem.isalpha() and
#                         not elem.isupper(), this_str))

print(list(filter(lambda x: x.isalpha() and not x.isupper(), 
                  input("Введите строку: "))))