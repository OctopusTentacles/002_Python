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

long_word = text[0]

for i in range(len(text)):
    if len(long_word) < len(text[i]):
        long_word = text[i]
        print(long_word)

# long_word = [index if len(index) > len(long_word) for index in text:]


