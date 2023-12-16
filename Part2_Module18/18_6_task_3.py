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


my_request = requests.get("https://swapi.dev/api/starships/")
# print(my_request)
# results - список словарей всех кораблей:
if my_request.status_code == 200:

    json_ships = json.loads(my_request.text)
    # print(json_ships)
    all_starship = []
    for result in json_ships['results']:
        if result["name"] == "Millennium Falcon":
            url_ship = result["url"]

    my_request = requests.get(url_ship).json()
    print(my_request)