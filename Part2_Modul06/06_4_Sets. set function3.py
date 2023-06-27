# Задача 3. Различные цифры
# Напишите программу, которая находит все различные цифры в символьной строке. 
# Для решения используйте множество (цифры будут различные, 
# и поиск во множестве намного быстрее, чем в списке).

# Подсказка: можно использовать вот такое сравнение '0'<=x<='9'

# Пример:
# Введите строку: ab1n32kz2
# Различные цифры строки: 123

stroka = set(input('Введите строку: '))

for symbol in stroka:
    if '0'<= symbol <= '9':
        
        print(symbol)