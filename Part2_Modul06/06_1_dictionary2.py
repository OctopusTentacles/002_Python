# Задача 2. Студент
# Пользователь вводит фамилию, имя студента, город проживания, вуз, в 
# котором он учится, и все его оценки. Всё вводится в одну строку через пробел. 
# Напишите программу, которая по этой информации составит словарь и выведет его на экран.

# Пример:
# Введите информацию о студенте через пробел 
# (имя, фамилия, город, место учёбы, оценки): Илья Иванов Москва МГУ 5 4 4 4 5

# Результат: 
# Имя - Илья
# Фамилия - Иванов
# Город - Москва
# Место учёбы - МГУ
# Оценки - [5, 4, 4, 4, 5]

info = input(
    'Введите информацию о студенте через пробел\n'
    '(имя, фамилия, город, место учёбы, оценки): '
)

info_list = info.split()
info_dict = dict()

info_dict['Имя'] = info_list[0]
info_dict['Фамилия'] = info_list[1]
info_dict['Город'] = info_list[2]
info_dict['Место учёбы'] = info_list[3]
info_dict['Оценки'] = [int(idx) for idx in info_list[4:]]

for key in info_dict:
    print(key, '-', info_dict[key])