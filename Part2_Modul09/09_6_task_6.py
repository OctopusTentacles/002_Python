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
        file_list = read_file.readlines()
    print(file_list)


# MAIN_CODE==========================================================
# chr(1040 1071) - RUS  chr(1072 1103) - rus 
# chr(65 90) - ENG      chr(97 122) - eng 
# alphabet_ru = ''.join(chr(i) for i in range(1040, 1104))
# print(alphabet_ru)

current_directory = os.path.dirname(__file__)
print(current_directory)


with zipfile.ZipFile((os.path.join(current_directory, 'voina-i-mir.zip')), 'r') as zf:
    zf.extractall('voina-i-mir.txt')


read_file(current_directory, 'second_tour.txt')

