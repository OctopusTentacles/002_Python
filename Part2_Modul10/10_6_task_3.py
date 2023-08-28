# Задача 03. Регистрация
# Что нужно сделать
# У вас есть файл с протоколом регистраций пользователей на 
# сайте — registrations.txt. Каждая строка содержит имя, емейл и возраст, 
# разделённые пробелами. Например: Василий test@test.ru 27.

# Напишите программу, которая проверяет данные из файла для каждой строки:

# Присутствуют все три поля.
# Поле «Имя» содержит только буквы.
# Поле «Имейл» содержит @ и . (точку).
# Поле «Возраст» является числом от 10 до 99.
# В результате проверки сформируйте два файла:

# registrations_good.log — для правильных данных, 
# записывать строки в том виде, как есть;
# registrations_bad.log — для ошибочных, записывать строку и вид ошибки.
# Для валидации строки данных напишите функцию, которая может выдавать исключения:

# НЕ присутствуют все три поля: IndexError.
# Поле «Имя» содержит НЕ только буквы: NameError.
# Поле «Имейл» НЕ содержит @ и . (точку): SyntaxError.
# Поле «Возраст» НЕ является числом от 10 до 99: ValueError.
# Формат выходных данных

# Содержимое файла registrations_bad.log:
# Ольга kmrn@gmail.com 123		Поле «Возраст» НЕ является числом от 10 до 99
# Чехова kb@gmail.com 142		Поле «Возраст» НЕ является числом от 10 до 99
# ……
# Степан ky 59		Поле «Имейл» НЕ содержит @ и . (точку)
# ……

# Содержимое файла registrations_good.log:
# Геннадий ttdababmt@gmail.com 69
# Ольга ysbxur@gmail.com 20
# ……

import os


def check_line(list_line):
    # field = 0

    # for index, value in enumerate(list_line):
        
        try:
            if list_line[0].isalpha():
                # field += 1
                
                try:
                    if ('@' and '.') in list_line[1]:
                        # field += 1
                        try:
                            if 9 < int(list_line[2]) < 100:
                                return True
                                # field += 1

                            else:
                                raise ValueError('Поле «Возраст» НЕ'
                                                 'является числом от 10 до 99')
                        except ValueError as exc:
                            return False

                    else:
                        raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
                except SyntaxError as exc:
                    return False
        
            else:
                raise NameError('Поле «Имя» содержит НЕ только буквы')
        except NameError as exc:
            return False
        except IndexError as exc:
            return False

    # if field == 3:
    # return True
         
    

def good_log(cur_dir, good_data):
    with open(os.path.join(cur_dir, 'registrations_good.log'), 
              'a', encoding='utf8') as good_file:
        good_file.write(str(good_data))
        return


def bad_log(cur_dir, bad_data):
        with open(os.path.join(cur_dir, 'registrations_bad.log'), 
              'a', encoding='utf8') as bad_file:
            bad_file.write(str(bad_data))
            return


def read_file(cur_dir, file_name):
    with open(os.path.join(cur_dir, file_name), 'r', encoding='utf8') as read_file:
        for i_line in read_file:
            list_registr = (i_line.rstrip()).split(' ')

            if check_line(list_registr):
                good_log(cur_dir, list_registr)

            else:
                bad_log(cur_dir, list_registr)



# MAIN_CODE==========================================================

# текущая директория 
current_directory = os.path.dirname(__file__)


# прочитать строки в файле
# создать лист для проверки
list_registration = read_file(current_directory, 'registrations.txt')



# проверить поля на правильность

# функция для исключений

# запись в файлы