# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
index = ''
adress = ''
info = ''
# business info
ogrnip = ''
inn = ''
account = ''
bank = ''
bik = ''
account2 = ''


def general_info_user(n_parameter, a_parameter, 
                      ph_parameter, e_parameter, i_parameter):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    if i:
        print('')
        print('Дополнительная информация:')
        print(i_parameter)


def business_info_user(ogrnip_parameter, inn_parameter, account_parameter, bank_parameter, bik_parameter, account2_parameter):
    print('\nИнформация о предпринимателе')
    print('ОГРНИП:', ogrnip_parameter)
    print('ИНН:', inn_parameter)
    print('Банковские реквизиты')
    print('Р/с:', account_parameter)
    print('Банк:', bank_parameter)
    print('БИК:', bik_parameter)
    print('К/с:', account2_parameter)



print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break



    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break

            # INPUT GENERAL INFO

            if option2 == 1:
                
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if a > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                ph = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        ph += ch
                e = input('Введите адрес электронной почты: ')
                index = input('Введите почтовый индекс: ')
                adress = input('Введите почтовый адрес (без индекса): ')
                i = input('Введите дополнительную информацию:\n')


            # INPUT BUSINESS INFO

            elif option2 == 2:                
                while True:
                    count = 0
                    ogrnip = input('Введите ОГРНИП: ')
                    for i in ogrnip:
                        count += 1                        
                    if count == 15:
                        break
                    print('ОГРНИП должен содержать 15 цифр')
                inn = input('Введите ИИН: ')
                while True:
                    count = 0
                    account = input('Введите расчетный счет: ')
                    for i in account:
                        count += 1                        
                    if count == 20:
                        break
                    print('Расчетный счет должен содержать 20 цифр')
                bank = input('Введите название банка: ')
                bik = input('Введите БИК: ')
                account2 = input('Введите корреспондентский счет: ')

            else:
                print('Введите корректный пункт меню')


    # SUBMENU 2: PRINT INFO

    elif option == 2:
        
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(n, a, ph, e, i)

            elif option2 == 2:
                general_info_user(n, a, ph, e, i)

                business_info_user(ogrnip, inn, account, bank, bik, account2)

            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
