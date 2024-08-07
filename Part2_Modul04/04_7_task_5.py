# Задание 5. Разворот
# На вход в программу подаётся строка, в которой буква h встречается как минимум два раза. 
# Реализуйте код, который разворачивает последовательность символов, заключённую 
# между первым и последним появлением буквы h, в противоположном порядке.

# Пример 1:
# Введите строку: hqwehrty
# Развёрнутая последовательность между первым и последним h: ewq.

# Пример 2:
# Введите строку: hh
# Развёрнутая последовательность между первым и последним h: 

# Пример 3:
# Введите строку: hhqwerh
# Развёрнутая последовательность между первым и последним h: rewqh.

# Советы и рекомендации
# Индекс нужного элемента можно искать как вручную, так и при помощи готовых методов списка.


word = input('Введите строку: ')

left = word.index('h')
right = word.rindex('h')

print('Развёрнутая последовательность между первым и последним h:',
        word[(right - 1):left:-1])