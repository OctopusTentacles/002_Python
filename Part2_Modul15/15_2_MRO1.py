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
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Я - Робот {self.__class__.__name__}, модель - {self.model}"
    
    def operate(self, action):
        self.action = action
        print(action)


class CanFly:
    def __init__(self, hight, speed) -> None:
        self.hight = hight
        self.speed = speed
    
    def take_off(self):
        print("Robot take off")

    def to_fly(self):
        print("Robot flying")

    def land(self):
        print("Robot landing")


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
