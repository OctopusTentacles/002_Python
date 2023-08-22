# Задача 6. «Война и мир»

# разбор домашнего задания


def collect_stats(file_name):
    result = {}
    text_file = open(file_name, 'r', encoding='utf-8')
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():


file_name = 'voyna-i-mir.txt'
stats = collect_stats(file_name)
print(stats)