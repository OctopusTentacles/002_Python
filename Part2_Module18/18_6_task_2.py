# Задача 2. Регистрационные знаки
# В России для транспорта применяются регистрационные знаки нескольких видов.
# Общее в них то, что они состоят из цифр и букв. Причём используются только 12
# букв кириллицы, имеющих графические аналоги в латинском алфавите: 
# А, В, Е, К, М, Н, О, Р, С, Т, У и Х.

# У частных легковых автомобилей номера — это буква, три цифры, две буквы, 
# затем две или три цифры с кодом региона.
# У такси — две буквы, три цифры, затем две или три цифры с кодом региона.

# Напишите программу, которая в перечне номеров находит номера частных 
# автомобилей и номера такси.

# Пример перечня:
# 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'


import re


data_base = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

privat_num = re.findall(r"" ,data_base)
taxi_number = re.findall(r"" ,data_base)

print('Список номеров частных автомобилей:', privat_num)
print('Список номеров такси:', taxi_number)

# Результат:
# Список номеров частных автомобилей: ['А578ВЕ777', 'К901МН666']
# Список номеров такси: ['ОР233787', 'СТ46599']