# Задача Деление строки

word = 'Привет'

sym_list = list(word)

first_part = word[:len(sym_list) // 2]
first_part = first_part[::-1]
print(first_part)

second_part = word[len(sym_list) // 2:]
second_part = second_part[::-1]
print(second_part)

print(first_part + second_part)