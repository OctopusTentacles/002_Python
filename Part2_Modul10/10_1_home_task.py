# Задача 6. «Война и мир»

# разбор домашнего задания


def collect_stats(file_name):
    result = {}
    text_file = open(file_name, 'r', encoding='utf-8')
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


file_name = 'voyna-i-mir.txt'
stats = collect_stats(file_name)
print_stats(stats)