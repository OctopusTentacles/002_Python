import random


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель
    def __init__(self, name):
        super().__init__(name)
        self.magic_power = self.start_power * 3 #30

    def attack(self, target):
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        print("\t", self.name, "имеет hp:", round(self.get_hp()))

        self.set_hp(self.get_hp() - 1.2 * damage)
        super().take_damage(damage)
    
    def heal(self, target):
        print("\t", target.name, "получил лечение =", self.magic_power, end=' | ')
        target.set_hp(target.get_hp() + self.magic_power)
        # target.set_hp(heal_power)
        print("HP:", target.get_hp())
    
    def make_a_move(self, friends, enemies):
        print(self.name, end=' | ')
        print("Исцеление:", self.magic_power, "сила:", round(self.get_power(), 1))
        target_of_heal = friends[0]
        min_health = 140

        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_heal = friend
                min_health = target_of_heal.get_hp()

        if min_health < 120 :
            print("\tИсцеление", target_of_heal.name, "| HP:", round(target_of_heal.get_hp()))
            self.heal(target_of_heal)
        else:
            if not enemies:
                return
            for enemy in enemies:
                if enemy.__class__.__name__ == "MonsterBerserk" and enemy.get_hp() > 0:
                    print("\tАтакую", enemy.name, "| HP:", enemy.get_hp())
                    self.attack(enemy)
                    break
            else:
                print("Атакую того, кто стоит ближе -", end=" ")
                print(enemies[0].name, round(enemies[0].get_hp()))
                self.attack(enemies[0])
        print('\n')
        super().make_a_move(friends, enemies)

    def __str__(self):
        return f"Name: {self.name} | HP: {round(self.get_hp())}"


class Tank(Hero):
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель
    def __init__(self, name):
        super().__init__(name)
        # self.power = self.get_power() / 2   # наносит половину урона (self.__power)
        self.defense = 1
        self.shield = None
        

    def attack(self, target):
        damage = self.power / 2 # доспехи очень тяжелые - наносит половину урона
        
        if self.shield:
            print("сила танка с щитом", damage)
            target.take_damage(damage)
        else:
            print("сила танка без щита", damage)
            target.take_damage(damage)


    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage / self.defense))
        super().take_damage(damage)

    def shield_on(self):
            if self.shield:
                print("щит поднят", end=' ')
                print(f"броня: {self.defense}, атака: {self.power}")
            else:
                self.shield = True
                self.defense = 1 * 2
                self.power = round(self.get_power() / 2) # 2.5
                print("поднимаю щит", end=' | ')
                print(f"броня: {self.defense}, атака: {self.power}")

    def shield_off(self):
            if  self.shield == False:
                print("щит опущен", end=' ')
                print(f"броня: {self.defense}, атака: {self.power}")
            else:
                self.shield = False
                self.defense = 1 / 2
                self.power = round(self.get_power() * 2) # 10
                print("опускаю щит", end=' ')
                print(f"броня: {self.defense}, атака: {self.power}")

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        if not enemies:
            return
        
        if self.get_hp() < 120:
            self.shield_on()
            print(f"\tЗащищаюсь | защита: {self.defense}| HP: {round(self.get_hp())}| Power: {round(self.get_power())}")
            
        else:
            self.shield_off()
            for enemy in enemies:
                if enemy.__class__.__name__ == "MonsterBerserk" and enemy.get_hp() != 0:
                    print("\tАтакую", enemy.name, "| HP:", enemy.get_hp())
                    self.attack(enemy)
                    break
            else:
                print(f"\tАтакую ближнего {enemies[0].name}| HP: {round(enemies[0].get_hp())}")
                self.attack(enemies[0])

        print('\n')
        super().make_a_move(friends, enemies)
    
    def __str__(self):
        return f"Name: {self.name} | HP: {round(self.get_hp())}"
    



class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 1

    def attack(self, target):
        target.take_damage(self.get_power() * self.power_multiply)
        self.power_down()

    def power_up(self):
        self.power_multiply *= 2

    def power_down(self, target=None):
        if target:
            print(f"\tСнижаю силу атаки {target.name} | текущая атака: {target.get_power()}")
            target.set_power(target.get_power() * self.power_multiply / 2)
            print(f"\t{target.name} | атака: {target.get_power()}")
        else:    
            self.power_multiply /= 2
        

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage * (self.power_multiply / 2)))
        super().take_damage(damage)

    def make_a_move(self, friends, enemies):
        print(self.name, end=' | ')
        print("усиление:", self.power_multiply, "сила:", round(self.get_power(), 1))
        if not enemies:
            return
        
        for enemy in enemies:
            if (self.power_multiply < 1 and enemy.__class__.__name__ == 
                "MonsterBerserk" and enemy.get_hp() < 55 and enemy.get_hp() > 0):
                self.power_down(enemy)
                break
            



        if self.power_multiply < 1:
            print("\tусиливаюсь |", end=" ")
            self.power_up()
            print("усиление:", self.power_multiply,)

        else:
            for enemy in enemies:
                if (enemy.__class__.__name__ == "MonsterBerserk" and enemy.get_hp() > 50) or enemy.get_hp() > 70:
                    print("\tАтакую", enemy.name, "| HP:", round(enemy.get_hp()))
                    self.attack(enemy)
                    break

            else:
                print("усиление:", self.power_multiply, "усиливаюсь")
                self.power_up()
                print("\tусиление:", self.power_multiply,)

                # print("\tАтакую", enemie.name, "| HP:", enemie.get_hp())
                # self.attack(enemie)

        print('\n')
        super().make_a_move(friends, enemies)


    def __str__(self):
        return f"Name: {self.name} | HP: {round(self.get_hp())}"
