# Задача Деление строки

word = 'Привет'
result = []

sym_list = list(word)

first_part = sym_list[:len(sym_list) // 2]
first_part = first_part[::-1]
print(first_part)

second_part = sym_list[len(sym_list) // 2:]
second_part = second_part[::-1]
print(second_part)

result.extend(first_part)
result.extend(second_part)
print(result)