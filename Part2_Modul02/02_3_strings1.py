# Задача 1. Текстовый редактор: возвращение

# Мы продолжаем участвовать в разработке нового текстового редактора 
# и делать жизнь обычных пользователей чуть лучше. 
# В этот раз у нас стоит задача сделать фишку с поиском и заменой 
# символов в выделенной строчке. Например, человек что-то перечислял 
# в тексте, но ошибся и вместо точек с запятой использовал двоеточия. 
# Лингвисты негодуют.

# Пользователь вводит строку S. Напишите программу, 
# которая заменяет в строке все двоеточия (:) на точки с запятой (;). 
# Также подсчитайте количество замен и выведите ответ на экран 
# (и новую строку тоже). Для решения используйте список.

# Пример:
# Введите строку: гвозди:шурупы:гайки
# Исправленная строка: гвозди;шурупы;гайки
# Кол-во замен: 2

S = input('Введите строку: ')

text_list = list(S)
count = 0
index = 0

for symbol in text_list:
    if symbol == ':':
        text_list[index] = ';'
        count += 1
    index += 1

for i in text_list:
    print(i, end='')
print('\nКол-во замен: ',count)