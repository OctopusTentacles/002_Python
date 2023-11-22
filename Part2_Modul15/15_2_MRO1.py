# Задача 1. Снова роботы
# На военную базу привезли очередную партию роботов. И в этот раз не абы каких, 
# а летающих: разведывательного дрона и военного робота.

# Разведывательный дрон просто летает в поиске противника. При команде operate 
# он выводит сообщение «Веду разведку с воздуха» и передвигается немного вперёд.

# У летающего военного робота есть оружие, и при команде operate он выводит 
# сообщение о защите военного объекта с воздуха с помощью этого оружия.

# Напишите программу, которая реализует все необходимые классы роботов. 
# Сущности «Робот» и «Может летать» должны быть вынесены в отдельные классы. 
# Обычный робот имеет модель и может вывести сообщение 
# «Я — Робот». Объект, который умеет летать, дополнительно имеет атрибуты 
# «Высота» и «Скорость», а также может взлетать, летать и приземляться.


class Robot:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    def __str__(self):
        res = super().__str__()
        return res + "{self.__class__.__name__} модель - {self.model}"
    
    def operate(self):
        print('Я - Робот!')


class CanFly:
    def __init__(self, *args, **kwargs) -> None:
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч
    
    def take_off(self):
        self.altitude = 100
        self.velocity = 300

    def to_fly(self):
        self.altitude = 5000

    def land(self):
        self.altitude = 0
        self.velocity = 0

    def operate(self):
        super().operate()
        print('летим')

    def __str__(self):
        res = super().__str__()
        return res + ' {} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity,
        )


class ScouteDrone(Robot, CanFly):
    def __init__(self, model):
        super().__init__(model)

    def operate(self, action=None):
        super().operate("Веду разведку с воздуха")
        super().to_fly()


class WarDrone(Robot, CanFly):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def operate(self, action=None):
        super().operate("активация {} в охранный режим для охраны с воздуха".format(
            self.weapon))

# =======================================================================================
scoute_drone = ScouteDrone("AIR-0007")
print(scoute_drone)
scoute_drone.take_off()
scoute_drone.operate()
scoute_drone.land()

wardrone = WarDrone("AIR-T-900", "Missle")
print(wardrone)
wardrone.take_off()
wardrone.operate()
wardrone.land()
