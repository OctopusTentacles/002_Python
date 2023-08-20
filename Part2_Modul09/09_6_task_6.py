# Задача 6. «Война и мир»
# Что нужно сделать
# Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». 
# Это довольно объёмное произведение лежит в архиве voina-i-mir.zip. 
# Напишите программу, которая подсчитывает статистику по буквам (не только русского алфавита) 
# в этом романе и выводит результат на экран (или в файл). Результат должен быть 
# отсортирован по частоте встречаемости букв (по возрастанию или убыванию). 
# Регистр символов имеет значение.

# Архив можно распаковать вручную, но, если хотите, можете изучить 
# документацию по модулю zipfile (можно использовать и другой модуль) и 
# попробовать написать код, который будет распаковывать архив за вас.


import os
import zipfile


def read_file(cur_dir, file_name):
    with open(os.path.join(cur_dir, file_name), 'r') as read_file:
        for i_line in read_file.readlines():
            for i_sym in i_line:

                if (64 < ord(i_sym) < 91) or (96 < ord(i_sym) < 123) or \
                    1039 < ord(i_sym) < 123:

                    if i_sym in dict_symbol.keys():
                        dict_symbol[i_sym] += 1
                    else:
                        dict_symbol[i_sym] = 1
            
        print(dict_symbol)


def extract(cur_dir, ending_name):
    for i_elem in os.listdir(cur_dir):
        if i_elem.endswith(ending_name):
            with zipfile.ZipFile(os.path.join(cur_dir, i_elem), 'r') as zf:
                zf.extractall(cur_dir)



# MAIN_CODE==========================================================
# chr(1040 1071) - RUS  chr(1072 1103) - rus 
# chr(65 90) - ENG      chr(97 122) - eng 
# alphabet_ru = ''.join(chr(i) for i in range(1040, 1104))
# print(alphabet_ru)

dict_symbol = dict()

# текущая директория
current_directory = os.path.dirname(__file__)
print(current_directory)


# распаковываем архив zip 
extract(current_directory, '.zip')



read_file(current_directory, 'first_tour.txt')

