

flights = dict()

def create_flight():
    print('\nВведите данные рейса:')
    flight_number = input('XXXX - номер рейса: ')
    flight_date = input('ДД/ММ/ГГГГ - дата рейса: ')
    depart_time = input('ЧЧ:ММ - время вылета: ')
    flight_time = input('ЧЧ.ММ - длительность перелета: ')
    depart_city = input('XXX - аэропорт вылета: ')
    arrive_city = input('XXX - аэропорт назначения: ')
    flight_price = float(input('X.XX - стоимость билета: '))
    
    flights[flight_number] = {
        'flight_number': flight_number,
        'flight_date': flight_date,
        'depart_time': depart_time,
        'flight_time': flight_time,
        'depart_city': depart_city,
        'arrive_city': arrive_city,
        'flight_price': flight_price
    }
    info_flight = list(flights[flight_number].values())

    print('\nИнформация о рейсе', *info_flight, 'добавлена\n')
    
    return



def show_flights():
    ...



def search_flight():
    ...



# MAIN MENU
def main_menu():
    while True:    
        print('Сервис поиска авиабилетов\n\n')
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
