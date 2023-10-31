# Type Annotations


from collections.abc import Iterable
from typing import List, Dict, Tuple


class Person:

    def __init__(self, name: str, age: int, friends: list) -> None:
        self.__name = name
        self.__age = age
        self.__friends = friends

    def __init__(self, name: str, age: int, friends: List[Person]) -> None:
        pass

    def __init__(self, name: str, age: int, friends: Dict[int, Person]) -> None:
        pass


    def __str__(self) -> str:
        pass


def fibonacci(number: int) -> Iterable[int]:
    a, b = 0, 1
    for _ in range(number):
        yield a
        a, b = b, a + b


from typing import Any

def any_type(elem: Any) -> None:
    print(elem)


from typing import Union

def to_dict(self) -> Dict[str, Union[str, int, List[dict]]]:
    return {
        "name": self.__name,
        "age": self.__age,
        "friends": [i_person.to_dict() for i_person in self.__friends]
    }


from typing import Optional
# Optional[...] - это сокращение конструкции Union[..., None]. 
# То есть, например, вместо Union[None, Any] стоит писать Optional[Any].
class Point:
    def __init__(self, value: Optional[Any], another: Optional['Point']) -> None:
        pass
# Здесь мы обратим внимание на две вещи. 
# Во-первых, вместо value: Any мы использовали value: Optional[Any], 
# то есть value может содержать None, либо что-то другое
# Во-вторых, в записи Optional[‘Point’] объект класса взят в одинарные кавычки. 
# Если их убрать, то PyCharm пожалуется на то, что Point ещё не объявлен, 
# а мы его уже используем. Иногда такая запись также имеет место быть.