# Задача 8. Бегущая строка

# В одной из практических работ вы писали для табло программу, 
# которая циклически сдвигает элементы списка чисел вправо на K позиций. 
# В этот раз вы работаете с двумя строками. Нужно проверить, не равна ли 
# на самом деле одна другой. Возможно, одна из них просто немного сдвинута.

# Пользователь вводит две строки. Напишите программу, которая определяет, 
# можно ли первую строку получить из второй циклическим сдвигом.

# Опционально: если получить можно, то выведите значение этого сдвига.

# Пример 1:
# Первая строка: abcd
# Вторая строка: cdab
# Первая строка получается из второй со сдвигом 2.

# Пример 2:
# Первая строка: abcd
# Вторая строка: cdba
# Первую строку нельзя получить из второй с помощью циклического сдвига.


# 1______________________________________________________________________

def shifting(text_1, text_2):
    shift = text_2.index(text_1[0])
    
    for symbol in text_2:
        if symbol in text_1 and (
            symbol == text_1[(text_2.index(symbol) + shift) % len(text_1)]):
                continue
        else:
            return print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
            
    return print(f'Первая строка получается из второй со сдвигом {shift}.')


text_1 = input('Первая строка: ')
text_2 = input('Вторая строка: ')

if len(text_1) == len(text_2) and text_1[0] in text_2:
    shifting(text_1, text_2)
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
   

# 2_____________________________________________________________________

text_1 = input('Первая строка: ')
text_2 = input('Вторая строка: ')

for i_shift in range(len(text_2)):
    if text_1 == text_2:
        print(f'Первая строка получается из второй со сдвигом {i_shift}.')
        break
    text_1 = text_1[1:] + text_1[0]
            
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')