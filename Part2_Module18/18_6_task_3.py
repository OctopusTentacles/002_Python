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


def api_info(url, name):

    response = requests.get(url)
    # print(my_request)
    # results - список словарей всех кораблей:
    if response.status_code == 200:
        ship_data = json.loads(response.text)

        for result in ship_data['results']:
            if result["name"] == name:
                starship_info = {
                    "название": result["name"], 
                    "максимальная скорость": result["max_atmosphering_speed"],
                    "класс": result["starship_class"],
                    "список пилотов": []                    
                }

                for url_pilot in result["pilots"]:
                    request_pilot = requests.get(url_pilot)
                    if request_pilot.status_code == 200:
                        pilot_data = json.loads(request_pilot.text)
                        pilot_info = {
                            "имя": pilot_data["name"],
                            "рост": pilot_data["height"],
                            "вес": pilot_data["mass"],
                            "родная планета": "",
                            "ссылка на информацию о родной планете": pilot_data["homeworld"]
                        }
                    request_planet = requests.get(pilot_data["homeworld"])
                    if request_planet.status_code == 200:
                        planet_data = json.loads(request_planet.text)
                        pilot_info["родная планета"] = planet_data["name"]
                        starship_info["список пилотов"].append(pilot_info)
        print(starship_info)
        # return starship_info
    



my_url = "https://swapi.dev/api/starships/"
search_name = "Millennium Falcon"

starship = api_info(my_url, search_name)
if starship:
    # print(json.dumps(starship, indent=4))



    with open(os.path.join(cur_dir, "info.json"), "w") as file:
        json_falcon = json.dump(starship, file, indent=4)

# with open(os.path.join(cur_dir, "info.json"), "r") as file:
#     print(json.load(file))
