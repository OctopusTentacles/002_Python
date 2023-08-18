# Задача 4. Турнир
# Что нужно сделать
# В файле first_tour.txt записано число K и данные об участниках турнира 
# по настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных 
# в первом туре. Во второй тур проходят участники, которые набрали более 
# K баллов в первом туре. 

# Напишите программу, которая выводит в файл second_tour.txt 
# данные всех участников, прошедших во второй тур, с нумерацией. 

# В первой строке нужно вывести в файл second_tour.txt 
# количество участников второго тура. Затем программа должна вывести 
# фамилии, инициалы и количество баллов всех участников, 
# прошедших во второй тур, с нумерацией. Имя нужно сократить до одной буквы. 
# Список должен быть отсортирован по убыванию набранных баллов.

# Пример:
# Содержимое файла first_tour.txt:
# 80
# Ivanov Serg 80
# Sergeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78

# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92


import os


def find_file(cur_path, file_name):
    for i_dir in os.listdir(cur_path):
        found_path = os.path.join(cur_path, i_dir)
        if i_dir == file_name:
            return os.path.abspath(found_path)
        elif os.path.isdir(found_path):
            result = find_file(found_path, file_name)
            if result:
                return result
            

def read_file(cur_path):
    file_content = list()

    r_file = open(cur_path, 'r', encoding='utf8')
    for i_line in r_file:

        line = i_line.split()
        file_content.append(line)
        print(i_line, end='')
    r_file.close
    
    return file_content[1:], file_content[:1]
# With...as обрабатывает открытие/закрытие ресурсов; закрывает 
# автоматически часть приложения, с которой больше не нужно работать
    # with open(cur_path) as r_file:
    #     for i_line in r_file.readlines(): # прочитать все строки (list)
    #         print(i_line, end='')
# хотел сделать красиво - print(*r_file.readlines()) без цикла, но слева
# получаются пробелы и убрать их не смог. lstrip() никуда не встает )))



def quick_sort(data):
    if not data:
        return data
    main_elem = int(data[-1][-1])

    low_main = [elem for _, elem in enumerate(data) if int(elem[-1]) < main_elem]
    equal_main = [elem for _, elem in enumerate(data) if int(elem[-1]) == main_elem]
    high_main = [elem for _, elem in enumerate(data) if int(elem[-1]) > main_elem]

    return quick_sort(high_main) + equal_main + quick_sort(low_main)



def write_file(cur_path, file_name, content):
    sort_content = quick_sort(content)

    w_file = open(os.path.join(cur_path, file_name), 'w', encoding='utf8')
    w_file.write(str(len(sort_content)) + '\n')

    for key, value in enumerate(sort_content):
        w_file.write(str(key + 1) + ') ' + str(value) + '\n')


# start_________________________________________________________________________
first_tour_file = find_file('..', 'first_tour.txt')
work_dir, file_name_1 = os.path.split(first_tour_file)


print('\nСодержимое файла first_tour.txt:')
content, rise_limit = read_file(first_tour_file)


rise_limit = (rise_limit.pop())
new_content = [value 
               for _, value in enumerate(content) 
               if int(rise_limit[0]) < int(value[-1])]


print('\nСодержимое файла second_tour.txt:')
write_file(work_dir, 'second_tour.txt', new_content)