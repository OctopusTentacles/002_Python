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
            

first_tour_file = find_file('..', 'first_tour.txt')
print(first_tour_file)