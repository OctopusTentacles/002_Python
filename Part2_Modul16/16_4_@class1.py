# Задача 1. Createtime
# Реализуйте декоратор класса, который выдаёт дату и время создания, 
# а также список всех методов объекта класса каждый раз, когда объект класса 
# создаётся в основном коде.


class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(self.max_num)])
        return result
    
    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num**3 for i_num in range(self.max_num)])
        return result



my_funcs_1 = Functions(max_num=1000)
my_funcs_2 = Functions(max_num=2000)
my_funcs_3 = Functions(max_num=3000)