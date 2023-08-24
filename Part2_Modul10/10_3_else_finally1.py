# Задача 1. Простая программа
# Напишите программу, которая открывает файл и записывает туда введённую 
# пользователем строку. Используйте операторы try except else finally. 
# Обработайте возможные ошибки:

# Проблема при открытии файла.
# Нельзя преобразовать данные в целое.
# Неожиданная ошибка.


import os

file = None
try:
    file = open(os.path.join(os.path.dirname(__file__), '23.3.txt'), 'w', encoding='utf8')
    number = int(input('Введите текст: '))
    file.write(str(number))
except (FileNotFoundError, PermissionError) as exc:
    print(type(exc), exc)
except ValueError as exc:
    print(type(exc), exc)
except Exception as exc:
    print(type(exc), exc)

else:
    print("Запись прошла без ошибок")

finally:
    if file and not file.closed:
        file.close()