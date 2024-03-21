

print('Сервис поиска авиабилетов\n\n')
flights = dict()


def create_flight():
    print('\nВведите данные рейса:')
    flight_number = input('XXXX - номер рейса: ').upper()
    flight_date = input('ДД/ММ/ГГГГ - дата рейса: ')
    depart_time = input('ЧЧ:ММ - время вылета: ')
    flight_time = input('ЧЧ.ММ - длительность перелета: ')
    depart_city = input('XXX - аэропорт вылета: ').upper()
    arrive_city = input('XXX - аэропорт назначения: ').upper()
    flight_price = float(input('X.XX - стоимость билета: '))
    
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


def show_flights():
    if flights:
        for flight_number in flights:
            info_flight = (flights[flight_number])
            print('Информация о рейсе', *info_flight)
    else:
        print('Информация о рейсах отсутствует')
    print()
    return


def search_flight():
    if flights:
        flight_number = input('Введите номер рейса в формате XXXX: ').upper()
        if flight_number in flights:
            info_flight = (flights[flight_number])
            print('Информация о рейсе', *info_flight)
        else:
            print('Рейс', flight_number, 'не найден')
    else:
        print('Информация о рейсах отсутствует')
    
    print()
    return



# MAIN MENU
def main_menu():
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


main_menu()
