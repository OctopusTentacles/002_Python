def foo(x):
    if x == 0:
        print("Вызов foo(0) возвращает 0")
        return 0
    else:
        print(f"Вызов foo({x - 1}) начинается и добавляется в стек")
        new_result = foo(x - 1)
        print(f"Вызов foo({x - 1}) завершился и удаляется из стека")
        result = x + new_result
        return result

print(f"Вызов foo(2) начинается и добавляется в стек")
result = foo(2)
print(f"Вызов foo(2) завершается и удаляется из стека")
print("Итоговый ответ — ", result)

# Рассмотрим нашу функцию подробнее:
def foo(x):
    if x <= 0:
        return 0
    else:
        new_result = foo(x - 1)
        result = x + new_result
        return result


print(foo(2))

# Запускается foo(2).
# Срабатывает else, так как 2 больше 0.

# Пайтон начинает выполнять первую строку внутри else:
# new_result = foo(2-1).

# В этой строке у нас целых три действия.

# 2-1
# foo(1)
# new_result =
# И, что интересно, пайтон выполнит первое действие и посчитает 2-1.
# Это нужно, чтобы запустить функцию foo(1). Но после запуска функция foo(2) 
# будет поставлена на паузу, и действие new_result = будет выполнено после того, 
# как завершится действие foo(1). Следующие строки тоже не будут выполнены, пока функция foo(2) приостановлена!

# Идём дальше. Запускается foo(1).
# Опять срабатывает else, так как 1 больше 0.

# Пайтон доходит до строки:
# new_result = foo(1-1)
# Выполняет foo(1-1) → foo(0).

# Теперь функция foo(1) тоже приостановлена!
# Управление переходит к foo(0).
# Срабатывает условие if x<= 0, так как 0 равен 0. 
# Срабатывает return 0.
# И этот return:

# завершает работу функции foo(0);
# возвращает число 0 туда, где была вызвана функция foo(0), а значит возвращает 0 в вызов foo(1).
# Пайтон снимает с паузы функцию foo(1)
# и продолжает с того места, на котором остановился:
# new_result = 0;
# result = 1+0  (x в текущем вызове по-прежнему равен 1);
# return 1 — этот return завершает функцию foo(1). 

# Функция foo(1) удаляется из стека, а пайтон снимает с паузы оригинальный вызов foo(2).

# Снова выполнение продолжается с того места, на котором мы остановились:

# new_result = 1 — тут мы вызывали foo(1); выше мы посчитали, что результат foo(1) был равен числу 1;
# result = 2+1  (x в текущем вызове по-прежнему равен 2);
# return 3 — этот return завершает функцию foo(2). 

# Из стека удаляется функция foo(2),
# а результат её выполнения попадает в строку, в которой была вызвана эта функция:
# print(foo(2)) — то есть сюда.

# И, наконец, мы распечатываем число 3 :)

            # Основные моменты
            # Рекурсия — это многократный вызов обычных функций.
            # Чтобы она сработала, в первую очередь, надо добавить условие выхода из рекурсии.