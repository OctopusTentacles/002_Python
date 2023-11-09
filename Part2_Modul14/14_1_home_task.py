# Задача 4. Односвязный список

# класс Узел:
#    - значение
#    - ссылка на след. узел

# класс Односвязный список:
#    - указатель на первый узел


from typing import Any, Optional


class Node:
    def __init__(self, value: Optional[Any] = None, next: Optional[Node] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return "Node [{value}]".format(value=str(self.value))