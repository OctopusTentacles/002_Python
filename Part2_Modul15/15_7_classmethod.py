# 15.7 Методы класса: декоратор classmethod

class Pet:
    def __init__(self) -> None:
        self.__legs = 4
        self.__tail = True

    def __str__(self) -> str:
        tail = "да" if self.__tail else "нет"
        return "Всего ног: {legs}\nХвост присутствует - {has_tail}".format(
            legs=self.__legs,
            has_tail=tail
        )
    

class Cat(Pet):
    # @staticmethod
    @classmethod
    def sound(cls) -> None:
        print("Мяу")


class Dog(Pet):
    def sound(self) -> None:
        print("Гав")


Cat.sound()