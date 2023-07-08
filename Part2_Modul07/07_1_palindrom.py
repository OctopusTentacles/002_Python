# 7.1 Разбор домашнего задания
# Palindrom


def palindron(string):
    char_dict = {}
    for i_sym in string:
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1

    odd_count = 0
    for i_value in char_dict.values():
        if i_value % 2 != 0:
            odd_count += 1
    return odd_count <= 1

word = (input('Введите слово: '))

if palindron(word):     
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
