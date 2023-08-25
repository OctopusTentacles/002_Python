# Задача 2. Логирование
# Возможно, вы замечали, что некоторые программы не просто выдают ошибку 
# и закрываются, но и записывают эту ошибку в файл. Таким образом проще 
# сформировать отчёт об ошибках, а значит, программисту будет проще их 
# исправить. Это называется логированием ошибок.

# Дан файл words.txt, в котором построчно записаны слова. 
# Необходимо определить количество слов, из которых можно получить 
# палиндром (привет предыдущим модулям). 
# Если в строке встречается число, то программа выдаёт ошибку 
# ValueError и записывает эту ошибку в файл errors.log

import os
count_poli = 0

def palindrom(word):
    return word == word[::-1]


current_dir = os.path.dirname(__file__)

with open(os.path.join(current_dir, 'words.txt'), 'r', encoding='utf8') as file, \
    open(os.path.join(current_dir, 'errors.log'), 'w', encoding='utf8') as log_file:

    for line in file:
        try:
            clear_line = line.rstrip()
            if clear_line.isalpha():
                count_poli += palindrom(clear_line)
            else:
                