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
ogrnip = 0
inn = 0
account = 0
bank = ''
bik = 0
account2 = 0


def general_info_user(name_parameter, age_parameter, 
                      phone_parameter, email_parameter,
                      index_parameter, adress_parameter, info_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', index_parameter)
    print('Адрес:  ', adress_parameter)
    if info:
        print('')
        print('Дополнительная информация:')
        print(info_parameter)


def business_info_user(ogrnip_parameter, inn_parameter, account_parameter, 
                       bank_parameter, bik_parameter, account2_parameter):
    print('\nИнформация о предпринимателе')
    print('ОГРНИП:', ogrnip_parameter)
    print('ИНН:   ', inn_parameter)
    print('Банковские реквизиты')
    print('Р/с:   ', account_parameter)
    print('Банк:  ', bank_parameter)
    print('БИК:   ', bik_parameter)
    print('К/с:   ', account2_parameter)



print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')


# MAIN MENU
while True:    
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break


    # SUBMENU 1: EDIT INFO
    if option == 1:
        
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break

            # INPUT PRIVAT INFO
            if option2 == 1:
                
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                user_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in user_phone:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch
                email = input('Введите адрес электронной почты: ')
                user_index = input('Введите почтовый индекс: ')
                for symbol in user_index:
                    if '0' <= symbol <= '9':
                        index += symbol
                adress = input('Введите почтовый адрес (без индекса): ')
                info = input('Введите дополнительную информацию:\n')


            # INPUT BUSINESS INFO
            elif option2 == 2:                
                while True:
                    count = 0
                    ogrnip = int(input('Введите ОГРНИП: '))
                    while ogrnip > 0:
                        ogrnip //= 10
                        count += 1                        
                    if count == 15:
                        break
                    print('ОГРНИП должен содержать 15 цифр')
                inn = int(input('Введите ИИН: '))
                while True:
                    count = 0
                    account = int(input('Введите расчетный счет: '))
                    while account > 0:
                        account //= 10
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
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            
            if option2 == 1:
                general_info_user(name, age, phone, email, index, adress, info)

            elif option2 == 2:
                general_info_user(name, age, phone, email, index, adress, info)
                business_info_user(ogrnip, inn, account, bank, bik, account2)

            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
