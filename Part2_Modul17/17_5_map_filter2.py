# Задача 2. Однострочный код 2
# Пользователь вводит строку, состоящую из любых символов. Напишите код, 
# который выводит на экран список этих символов, 
# исключая цифры и буквы в верхнем регистре.

# Пример работы консоли:
# Введите строку: qWe456rtY

# ['q', 'e', 'r', 't']

from typing import List


this_str = input("Введите строку:")

list_str = [sym for sym in this_str]

list_str = list(filter(lambda elem: elem.isdigit, list_str))

print(list_str)