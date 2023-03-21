
while True:
    for attempt in range(1, 4):
        pincode = int(input('Введите пинкод: '))
        if pincode == 1234:
            print('Пин-код верный. Получите зарплату.')
            break
        print('Пин-код неверный. осталось попыток', 3 - attempt)
    else:
        print('Ваша карта заблокирована. До свидания.')
    print()
    print('Следующий клиент, добро пожаловать!')
