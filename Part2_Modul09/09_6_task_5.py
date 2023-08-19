# Задача 5. Частотный анализ
# Что нужно сделать
# Есть файл text.txt, который содержит текст. Напишите программу, 
# которая выполняет частотный анализ, определяя долю каждой буквы 
# английского алфавита в общем количестве английских букв в тексте, 
# и выводит результат в файл analysis.txt. Символы, не являющиеся 
# буквами английского алфавита, учитывать не нужно. 

# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, 
# с тремя знаками в дробной части. Буквы должны быть отсортированы по 
# убыванию их доли. Буквы с равной долей должны следовать в алфавитном порядке.

# Пример:
# Содержимое файла text.txt:
# Mama myla ramu.

# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083

import os


def new_file(cur_dir, file_name):
    created_file = open(os.path.join(cur_dir, file_name), 'w', encoding='utf8')
    created_file.write('Mama myla ramu.')
    created_file.close()

    count = 0
   
    created_file = open(os.path.join(cur_dir, file_name), 'r', encoding='utf8')
    for i_line in created_file:
        for sym in i_line.lower():
            if sym in alfabet:
                count += 1
                if sym in dict_sym.keys():
                    dict_sym[sym] += 1
                else:
                    dict_sym[sym] = 1
    print(dict_sym)

    for key, value in dict_sym.items():
        dict_sym[key] = round(value / count, 3)
    print(dict_sym)



alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
dict_sym = dict()

files_dir = os.path.dirname(__file__)
new_file(files_dir, 'text.txt')



print(files_dir)