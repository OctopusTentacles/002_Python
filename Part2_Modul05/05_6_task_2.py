# Задача 2. Самое длинное слово

# Пользователь вводит строку, содержащую пробелы. Найдите в ней самое 
# длинное слово, выведите это слово и его длину. Если таких слов несколько, 
# выведите первое из них.

# Пример 1:
# Введите строку: я есть строка
# Самое длинное слово: строка
# Длина этого слова: 6

# Пример 2:
# Введите строку: а б
# Самое длинное слово: а
# Длина этого слова: 1

# Пример 3:
# Введите строку:    б
# Самое длинное слово: б
# Длина этого слова: 1


text = input('Введите строку: ').split()

long_word = ''

for index in range(len(text)):
    if len(long_word) < len(text[index]):
        long_word = text[index]
        
print('Самое длинное слово:', long_word)
print('Длина этого слова:', len(long_word))


