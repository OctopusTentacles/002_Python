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


def api_info(url, info, name):

    my_request = requests.get(url)
    # print(my_request)
    # results - список словарей всех кораблей:
    if my_request.status_code == 200:

        json_data = json.loads(my_request.text)
        # print(json_ships)
        for result in json_data['results']:
            if result["name"] == name:
                dict_info = {}
                for key_1 in info:
                    # if key_1 == "pilots":
                    #     for key_2 in pilot_info:
                    #         dict_info[key_1][key_2] = result[key_1](key_2)
                    dict_info[key_1] = result[key_1]
                print(dict_info)


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



ship_info = ["name", "max_atmosphering_speed", "starship_class", "pilots"]
pilot_info = ["name", "height", "mass", "homeworld", "homeworld"]

starship = api_info(my_url, ship_info, search_name)