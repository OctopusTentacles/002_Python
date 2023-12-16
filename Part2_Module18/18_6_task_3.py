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

url = "https://swapi.dev/api/starships/"
search_name = "Millennium Falcon"

my_request = requests.get(url)
# print(my_request)
# results - список словарей всех кораблей:
if my_request.status_code == 200:

    json_ships = json.loads(my_request.text)
    # print(json_ships)
    for result in json_ships['results']:
        if result["name"] == search_name:

            ship_info = {'name': result["name"], 
                         "max_atmosphering_speed": result["max_atmosphering_speed"],
                         "starship_class": result["starship_class"],
                         "pilots": result["pilots"]
                         }
            print(ship_info)

            # falcon_ship = requests.get(result["url"])
            # json_dict = json.loads(falcon_ship.text)
            # ship_info = json_dict.get("name", )

            # with open(os.path.join(cur_dir, "falcon.json"), "w") as file:
            #     json_falcon = json.dump(json_dict, file, indent=4)

            
            # print(json_falcon)

