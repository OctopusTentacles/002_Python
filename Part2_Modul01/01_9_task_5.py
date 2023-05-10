# Задача 5. Годы
# Что нужно сделать
# Недавно Костя прочитал научно-фантастическую книгу. 
# В ней самые страшные события случались только тогда, 
# когда в году были три одинаковые цифры. Косте стало 
# интересно, какие годы были или будут «особенными» в определённом промежутке.

# Напишите программу, в которой у пользователя запрашивается 
# два четырёхзначных числа A и B. Затем выведите в порядке 
# возрастания все четырёхзначные числа в интервале от A до B, 
# запись которых содержит ровно три одинаковые цифры.

# Пример работы программы:

# Введите первый год: 1900
# Введите второй год: 2100

# Годы от 1900 до 2100 с тремя одинаковыми цифрами:
# 1911
# 1999
# 2000
# 2022

def years(a, b):
    for i in range(a, b + 1):
            year = i
            four = year % 10
            year //= 1000
            three = year % 10
            year //= 100
            two = year % 10
            one = year // 10
            if (one == two == three) or (one == two == four) or (two == three == four):
                 print(i)






year_1 = int(input('Введите первый год: '))
year_2 = int(input('Введите второй год: '))
if year_1 > year_2:
    year_1, year_2 = year_2, year_1
years(year_1, year_2)
