# Задание 7. IP-адрес 2

# При написании клиент-серверного приложения часто приходится работать 
# с IP-адресами. Как вы уже знаете, IP-адрес состоит из четырёх целых чисел 
# в диапазоне от 0 до 255, разделённых точками.

# Пользователь вводит строку. Напишите программу, которая определяет, 
# действительно ли заданная строка — правильный IP-адрес. 
# Обеспечьте контроль ввода, где предусматривается добавление целых 
# чисел от 0 до 255 и точек между ними.

# Пример 1
# Введите IP: 128.16.35.a4
# a4 — это не целое число.

# Пример 2
# Введите IP: 240.127.56.340
# 340 превышает 255.

# Пример 3
# Введите IP: 34.56.42,5
# Адрес — это четыре числа, разделённые точками.

# Пример 4
# Введите IP: 128.0.0.255
# IP-адрес корректен.


def check_ip(ip):
    ip_list = ip.split('.')
    
    if len(ip_list) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
        return False

    for sym in ip_list:
        if not sym.isdigit():
            print(f'{sym} — это не целое число.')
            return False
        elif int(sym) > 255:
            print(f'{sym} превышает 255.')
            return False
        

while True:
    my_ip = input('Введите IP: ')
    if check_ip(my_ip):
        print('IP-адрес корректен.')