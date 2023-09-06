# ПОДКЛЮЧАЕМЫЕ МОДУЛИ

# ОСНОВНОЙ СКРИПТ


import garden



garden = garden.PotatoGarden(5)

for _ in range(3):
    garden.grow_all()

garden.are_all_ripe()