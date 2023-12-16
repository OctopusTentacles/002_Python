# Задача 3. May the force be with you
# Фанаты «Звёздных войн» (Star Wars) написали API по своей любимой вселенной. 
# Ссылка на документацию: Documentation.

# Внимательно изучите документацию этого API и напишите программу, 
# которая выводит на экран (и в JSON-файл) информацию о пилотах 
# легендарного корабля Millennium Falcon.

# Информация о корабле должна содержать следующие пункты:
# название,
# максимальная скорость,
# класс,
# список пилотов.

# Внутри списка о каждом пилоте должна быть следующая информация:
# имя,
# рост,
# вес,
# родная планета,
# ссылка на информацию о родной планете.


import os
import json
import requests


cur_dir = os.path.dirname(__file__)

my_url = "https://swapi.dev/api/starships/"
search_name = "Millennium Falcon"

ship_info = ["name", "max_atmosphering_speed", "starship_class", "pilots"]
pilot_info = ["name", "height", "mass", "homeworld", "homeworld"]

dict_info = {}

my_request = requests.get(my_url)
if my_request.status_code == 200:
    json_data = json.loads(my_request.text)

    for result in json_data["results"]:
        if result == search_name:
            


    # with open(os.path.join(cur_dir, "info.json"), "w") as file:
    #     json_falcon = json.dump(ship_info, file, indent=4)

    # with open(os.path.join(cur_dir, "info.json"), "r") as file:
    #     print(json.load(file))



# def api_info(url, info, name=None):

#     my_request = requests.get(url)
#     # print(my_request)
#     # results - список словарей всех кораблей:
#     if my_request.status_code == 200:

#         json_data = json.loads(my_request.text)
#         # print(json_ships)
#         for key_1 in info:

#         for result in json_data['results']:
#             if result["name"] == name:
#                 dict_info = {}
#                 for key_1 in info:
#                     if isinstance(result[key_1], list):
#                         for key_2 in result[key_1]:
#                             return api_info(key_2, pilot_info)
#                     dict_info[key_1] = result[key_1]
#                 print(dict_info)


            # ship_info = {'name': result["name"], 
            #              "max_atmosphering_speed": result["max_atmosphering_speed"],
            #              "starship_class": result["starship_class"],
            #              "pilots": result["pilots"]
            #              }
            # # print(ship_info)


            # with open(os.path.join(cur_dir, "info.json"), "w") as file:
            #     json_falcon = json.dump(ship_info, file, indent=4)

            # with open(os.path.join(cur_dir, "info.json"), "r") as file:
            #     print(json.load(file))



# ship_info = ["name", "max_atmosphering_speed", "starship_class", "pilots"]
# pilot_info = ["name", "height", "mass", "homeworld", "homeworld"]

# starship = api_info(my_url, ship_info, search_name)