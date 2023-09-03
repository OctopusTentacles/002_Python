# Задача 2. Однотипные объекты
# В офис заказали небольшую партию из четырёх мониторов и трёх наушников. 
# У монитора есть четыре характеристики: название производителя, 
# матрица, разрешение и частота обновления экрана. 
# Все четыре монитора отличаются только частотой.

# У наушников три характеристики: 
# название производителя, чувствительность и наличие микрофона. 
# Отличие только в наличии микрофона.

# Для внесения в базу программист начал писать такой код:
# Поправьте программиста: перепишите код, используя классы и экземпляры классов.


class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    resolution = 'WQHD'
    frequency = 0

class Headphones:
    name = 'Sony'
    sensitivity = 108
    microphone = True

monitors = [Monitor() for _ in range(4)]
headphones = [Headphones() for _ in range(3)]

for index, number in enumerate([60, 144, 70, 60]):
    monitors[index].frequency = number

headphones[0].microphone = False


# monitor_1 = Monitor()
# monitor_2 = Monitor()
# monitor_3 = Monitor()
# monitor_4 = Monitor()

# monitor_1.frequency = 60
# monitor_2.frequency = 144
# monitor_3.frequency = 70
# monitor_4.frequency = 60


# headphones_1 = Headphones()
# headphones_2 = Headphones()
# headphones_3 = Headphones()

# headphones_1.microphone = False
# headphones_2.microphone = True
# headphones_3.microphone = True
