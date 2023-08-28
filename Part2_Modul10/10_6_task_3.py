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
    field = 0

    for index, value in enumerate(list_line):
        

        if index == 0 and value.isalpha():
            field += 1
            continue

        if index == 1 and ('@' and '.') in value:
            field += 1
            continue
            
        if index ==2 and (9 < int(value) < 100):
            field += 1

        if field == 3:
            return True

    # try:
    #     # проверить имя________________________________________________
    #     if list_line[0].isalpha():
    #         good_str += list_line[0]
    #     else:
    #         raise NameError('Поле «Имя» содержит НЕ только буквы')
    # except NameError as exc:
    #         raise IndexError('НЕ присутствуют все три поля')
    # except IndexError:
    
    #     # проверить почту______________________________________________
    #     if ('@' and '.') in list_line[1]:
    #         good_str += list_line[1]
    #     else:
    #         raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
    # except SyntaxError as exc:
    #         raise IndexError('НЕ присутствуют все три поля')
    # except IndexError:
    #     print(exc)

    
    #     # проверить возраст___________________________________________
    #     if 9 < int(list_line[2]) < 100:
    #         good_str += list_line[2]
    #     else:
    #         raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
    # except ValueError as exc:
    #         raise IndexError('НЕ присутствуют все три поля')
    # except IndexError as exc:
    #     print(exc)
         
    # finally:
         
    




def good_log(cur_dir, good_data):
    with open(os.path.join(cur_dir, 'registrations_good.log'), 
              'a', encoding='utf8') as good_file:
        good_file.write(str(good_data))
        return



def read_file(cur_dir, file_name):
    with open(os.path.join(cur_dir, file_name), 'r', encoding='utf8') as read_file:
        for i_line in read_file:
            list_registr = (i_line.rstrip()).split(' ')

            if check_line(list_registr):
                good_log(cur_dir, list_registr)

            else:
                print(list_registr)



            


# MAIN_CODE==========================================================

# текущая директория 
current_directory = os.path.dirname(__file__)


# прочитать строки в файле
# создать лист для проверки
list_registration = read_file(current_directory, 'registrations.txt')



# проверить поля на правильность

# функция для исключений

# запись в файлы