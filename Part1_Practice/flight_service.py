""" Сервис поиска авиабилетов. """


# Словарь для хранения данных о рейсах:
flights = dict()

print('Сервис поиска авиабилетов\n\n')


def print_error():
    print('ОШИБКА! Используйте шаблон при вводе!')


def create_flight_number() -> str:
    """Ввод номера рейса."""
    while True:
        flight_number = input('XXXX - номер рейса: ').upper()
        if len(flight_number) != 4:
            print_error()
        else:
            return flight_number
        
def create_flight_date() -> str:
    """Ввод даты рейса."""
    while True:
        flight_date = input('ДД/ММ/ГГГГ - дата рейса: ')
        if len(flight_date) != 10:
            print_error()
        else:
            return flight_date
        
def create_depart_time() -> str:
    """Ввод времени вылета."""
    while True:
        depart_time = input('ЧЧ:ММ - время вылета: ')
        if len(depart_time) != 5:
            print_error()
        else:
            return depart_time
        
def create_flight_time() -> str:
    """Ввод длительности перелета."""
    while True:
        flight_time = input('ЧЧ.ММ - длительность перелета: ')
        try:
            0 <= float(flight_time)
        except ValueError:
            print_error()
            continue

        hours, minutes = flight_time.split('.')
        if len(hours) == 2 and len(minutes) == 2 and int(hours) >= 0:
            return flight_time
        else:
            print_error()
            
def create_depart_city() -> str:
    """Ввод кода аэропорта вылета."""
    while True:
        depart_city = input('XXX - аэропорт вылета: ').upper()
        if len(depart_city) != 3:
            print_error()
        else:
            return depart_city
        
def create_arrive_city() -> str:
    """Ввод кода аэропорта назначения."""
    while True:
        arrive_city = input('XXX - аэропорт назначения: ').upper()
        if len(arrive_city) != 3:
            print_error()
        else:
            return arrive_city
        
def create_flight_price() -> float:
    """Ввод стоимости билета."""
    while True:
        flight_price = float(input('.XX - стоимость билета: '))
        if flight_price > 0:
            return flight_price
        else:
            print_error()


# =====================================================================
def create_flight() -> None:
    """Создание нового рейса."""
    print('\nВведите данные рейса:')
    flight_number = create_flight_number()
    flight_date = create_flight_date()
    depart_time = create_depart_time()
    flight_time = create_flight_time()
    depart_city = create_depart_city()
    arrive_city = create_arrive_city()
    flight_price = create_flight_price()
    # Добавление информации о рейсе в словарь:
    flights[flight_number] = [
        flight_number,
        flight_date,
        depart_time,
        flight_time,
        depart_city,
        arrive_city,
        flight_price,
    ]
    info_flight = (flights[flight_number])
    print('\nИнформация о рейсе', *info_flight, 'добавлена\n')
    return


def show_flights() -> None:
    """Вывод информации о всех рейсах."""
    if flights:
        for flight_number in flights:
            info_flight = (flights[flight_number])
            print('Информация о рейсе:', *info_flight)
    else:
        print('Информация о рейсах отсутствует')
    print()
    return


def search_flight() -> None:
    """Поиск рейса по номеру."""
    if flights:
        flight_number = input('Введите номер рейса в формате XXXX: ').upper()
        if flight_number in flights:
            info_flight = (flights[flight_number])
            print('Информация о рейсе:', *info_flight)
        else:
            print('Рейс', flight_number, 'не найден')
    else:
        print('Информация о рейсах отсутствует')
    print()
    return


# MAIN MENU============================================================
def main_menu() -> None:
    """Главное меню программы."""
    while True:    
        print('Главное меню:\n')
        print('1 - ввод рейса')
        print('2 - вывод всех рейсов')
        print('3 - поиск рейса по номеру')
        print('0 - завершение работы')

        option = int(input('\nВведите номер пункта меню: '))
        if option == 1:
            create_flight()
        elif option == 2:
            show_flights()
        elif option == 3:
            search_flight()
        elif option == 0:
            print('\nПрограмма завершена!\n')
            break
        else:
            print('\nОшибка! Повторите ввод!\n')


# Запуск главного меню:
main_menu()
