# Задача 2. Соседи
# Дана строка S и номер позиции символа в строке. Напишите программу, 
# которая выводит соседей этого символа и сообщение о количестве 
# таких же символов среди этих соседей: их нет, есть ровно 
# один или есть два таких же.

# Пример 1:
# Введите строку: abbc
# Номер символа: 3

# Символ слева: b
# Символ справа: c

# Есть ровно один такой же символ.

 
# Пример 2:
# Введите строку: abсd
# Номер символа: 3

# Символ слева: b
# Символ справа: d

# Таких же символов нет.

S = input('Введите строку: ')
text_list = list(S)

symbol = int(input('Номер символа: '))
symbol_1 = symbol - 1
symbol_left = symbol_1 - 1
symbol_right = symbol

print('\nСимвол слева:', text_list[symbol_left])
print('Символ справа:', text_list[symbol_right])

if text_list[symbol_1] == text_list[symbol_left] == text_list[symbol_right]:
    print('Есть два таких же символа.')
elif (text_list[symbol_1] == text_list[symbol_left]) or (
    text_list[symbol_1] == text_list[symbol_right]):
    print('Есть ровно один такой же символ.')
else:
    print('Таких же символов нет.')
