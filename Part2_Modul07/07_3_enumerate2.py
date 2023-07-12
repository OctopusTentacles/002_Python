# Задача 2. Словари из списков
# Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита 
# (могут повторяться). Затем для каждого списка создайте словарь из пар 
# «индекс — значение» и выведите оба словаря на экран.
# Подсказка: random

# Пример: 
# Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
# Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']

# Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т', 7: 'ж', 8: 'е', 9: 'к'}
# Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}


import random
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

list_1 = [random.choice(alphabet) for _ in range(10)]
list_2 = [random.choice(alphabet) for _ in range(10)]

print(list_1)
print(list_2)
