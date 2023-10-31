# Type Annotations


from 


class Person:

    def __init__(self, name: str, age: int, friends: list) -> None:
        self.__name = name
        self.__age = age
        self.__friends = friends

    def __str__(self) -> str:
        pass


def fibonacci(number: int) -> Iterable[int]:
    a, b = 0, 1
    for _ in range(number):
        yield a
        a, b = b, a + b