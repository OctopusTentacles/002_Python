# Задача 6. «Война и мир»

# разбор домашнего задания

import os
import collections

def collect_stats(cur_dir, file_name):
    result = {}
    text_file = open(os.path.join(cur_dir, file_name), 'r', encoding='utf-8')
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()
    return result


def print_stats(stats):
    print('+{:-^19}+'.format('+')) 
    #сделать 19 символов поставив знак '+' по центру, а края заполнить знком '-'
    print('|{: ^9}|{: ^9}|'.format('буква', 'частота'))
    print('+{:-^19}+'.format('+'))
    for char, count in stats.items():
        print('|{: ^9}|{: ^9}|'.format(char, count))
    print('+{:-^19}+'.format('+'))


def sort_by_frequency(stats_dict):
    sorted_values = sorted(stats_dict.values())
    sorted_dict = collections.OrderedDict() 
    # Dictionary that remembers insertion order для запоминания сортировки словаря 
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key] == i_value:
                sorted_dict[j_key] = stats_dict[j_key]
    return sorted_dict



current_directory = os.path.dirname(__file__)
file_name = 'voyna-i-mir.txt'
stats = collect_stats(current_directory, file_name)
stats = sort_by_frequency(stats)
print_stats(stats)