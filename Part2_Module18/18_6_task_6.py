# Задача 6. Поиск разницы между двумя JSON-файлами (пример из реального 
# тестового задания на должность Python-разработчика уровня Junior)

# Найдите различия между двумя JSON-файлами. Если различающиеся параметры 
# входят в diff_list, выведите различие. Иными словами, вам нужно отловить 
# изменение определённых параметров и вывести значение: что изменилось и на что. 
# Набор ключей в обоих файлах идентичный, различаются лишь значения.

# Напишите программу, которая: 
# загружает данные из двух предложенных JSON-файлов (находятся в репозитории);
# выполняет сравнение параметров, указанных в diff_list;
# формирует результат в виде словаря;
# записывает словарь в JSON-файл с названием result.json.
# Исходные данные

# Файлы: 
# json_old.json,
# json_new.json.
# Список параметров для отслеживания (можно сформировать инпутом или ввести вручную):


import os
import re
import json
import requests

cur_dir = os.path.dirname(__file__)
diff_list = ["services", "staff", "datetime"]


def compare_dict(data_list, dict_1, dict_2, result_dict=None):
    """
    """
    if result_dict is None:
        result_dict = {}

    for key_1 in dict_1:
        if not key_1 in data_list and isinstance(dict_1[key_1], dict):
            compare_dict(data_list, dict_1[key_1], dict_2[key_1], result_dict)

        elif key_1 in data_list and dict_1[key_1] != dict_2[key_1]:
            result_dict[key_1] = dict_2[key_1]   

    return result_dict


# загрузить данные json:
def from_json(json_file):
    with open(os.path.join(cur_dir, json_file), "r", encoding="utf-8") as file:
        return(json.load(file))
    
def to_json(sourse):
    with open(os.path.join(cur_dir, "result.json"), "w") as file:
        json.dump(sourse, file, indent=4, ensure_ascii=False)

# MAIN===================================================================================
old_file = from_json("json_old.json")
new_file = from_json("json_new.json")

result = compare_dict(diff_list, old_file, new_file)

# записать словарь в JSON-файл с названием result.json.
to_json(result)

print(result)

# Результат:
# {'services': [{'id': 22222225, 
# 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 
# 'first_cost': 1500, 'amount': 1}], 'datetime': '2022-01-25T13:00:00+03:00'}