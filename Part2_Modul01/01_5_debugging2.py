# Задача 2. НОД

# Помните, мы писали функцию, которая находит наибольший 
# общий делитель двух чисел? Вот этот код:

# Теперь представьте ситуацию, что вам нужно объяснить 
# другому человеку, как этот код работает, шаг за шагом. 
# Предположим, на вход подаются числа 4782 и 698. Используя 
# только точку останова, определите, чему будет равняться 
# переменная а, когда переменная b станет равна двум.

def gcd(a, b):

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print('Наибольший общий делитель:', a + b)

gcd(30, 18)