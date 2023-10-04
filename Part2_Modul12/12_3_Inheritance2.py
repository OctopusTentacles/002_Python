# Задача 2. Роботы
# На военную базу завезли несколько интересных моделей роботов, 
# которые похожи между собой, но имеют немного разные функции. У каждого робота 
# есть номер модели и действие operate, которое означает, что делает робот. 
# Особенности роботов следующие:

# У робота-пылесоса есть мешок для мусора, изначально он пустой (0). 
# При команде operate робот сообщает, что он пылесосит пол, 
# и выводит текущую заполняемость мешка.

# У военного робота есть оружие, и при команде operate он выводит сообщение 
# о защите военного объекта с помощью этого оружия.

# Ещё есть робот — подводная лодка, который также является военным. 
# У этого робота есть значение глубины, и при команде operate он делает то же, 
# что и военный робот, плюс сообщает, что охрана ведётся под водой.

# Напишите программу, которая реализует все необходимые классы роботов.

class Robot:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Робот {self.__class__.__name__}, модель - {self.model}"
    
    def operate(self, action):
        self.action = action
        print("начинает...", action)


class VacuumRobot(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.bag = 0

    def operate(self, action=None):
        super().operate("пылесосить")
        self.bag += 1
        print("Состояние мешка:", self.bag)


class WarRobot(Robot):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def operate(self, action=None):
        super().operate("активацию {} в охранный режим".format(self.weapon))
        

class MarineRobot(WarRobot):
    def __init__(self, model, weapon, depth):
        super().__init__(model, weapon)
        self.depth = depth
        
    def operate(self, action=None):
        super().operate()    
        print("Глубина действий:", self.depth)


# =======================================================================================
vacuum = VacuumRobot("Voo123")
print(vacuum)
vacuum.operate()

warbot = WarRobot("WarT800", "Система Воздух-Земля")
print(f"\n{warbot}")
warbot.operate()

marine = MarineRobot("WarT3000", "ТОрпеды", 30)
print(f"\n{marine}")
marine.operate()