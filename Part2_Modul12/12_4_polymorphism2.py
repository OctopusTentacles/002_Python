# Задача 2. Полёт
# Иногда для реализации дочерних классов используется так называемый класс-роль, 
# где также описываются общие атрибуты и методы, но в программе инициализируются 
# объекты только дочерних классов, а базовый класс-роль не трогается. 
# К примеру, что общего у бабочки и ракеты? Они обе могут летать и приземляться. 

# Реализуйте класс «Может летать». 
# Атрибуты:
# Высота = 0.
# Скорость = 0.
# Методы:

# Взлететь (в теле прописать pass).
# Лететь (в теле прописать pass).
# Приземлиться (установить высоту и скорость в значение 0).
# Вывести высоту и скорость на экран.

# Затем реализуйте два дочерних класса: 
# «Бабочка», который может:
# Взлететь (высота = 1).
# Лететь (скорость = 0.5).

# «Ракета», которая может:
# Взлететь (высота = 500, скорость = 1000).
# Приземлиться (высота = 0, взрыв).
# Взорваться (тут уже что угодно).


class CanFly:
    def __init__(self):
        self.height = 0
        self.speed = 0

    def take_off(self):
        # TODO document why this method is empty
        pass

    def to_fly(self):
        # TODO document why this method is empty
        pass

    def to_land(self):
        self.__init__()

    def __str__(self):
        return "{}: высота - {}, скорость - {}".format(
            self.__class__.__name__, self.height, self.speed
        )
    

class Butterfly(CanFly):
    def take_off(self):
        print("Бабочка полетела")
        self.height = 1

    def to_fly(self):
        self.speed = 0.5


class Rocket(CanFly):
    def take_off(self):
        self.height = 500
        self.speed = 1000
        print("Ракета полетела")

    def to_land(self):
        print("Ракета падает")
        # self.height = 0
        # self.speed = 0
        self.explosion()

    def explosion(self):
        self.__init__()
        return print("Boooom")


# ========================================================================================
butterfly = Butterfly()
rocket = Rocket()

butterfly.take_off()
print(butterfly)
butterfly.to_fly()
print(butterfly)

rocket.take_off()
print(rocket)
rocket.to_land()
print(rocket)