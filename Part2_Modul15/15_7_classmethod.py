# 15.7 Методы класса: декоратор classmethod

class Pet:
    TOTAL_SOUNDS = 0

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
    @staticmethod
    def sound() -> None:
        print("Мяу")


class Dog(Pet):
    @classmethod
    def sound(cls) -> None:
        cls.TOTAL_SOUNDS += 1
        print(cls.TOTAL_SOUNDS)
        print("Гав")


Cat.sound()
Dog.sound()

dog = Dog()
Dog.sound()
Dog.sound()
