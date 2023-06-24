# Задание 5. Пароль

# При регистрации на сайте, помимо логина, нужно придумать пароль. 
# Этот пароль должен состоять минимум из восьми символов, 
# содержать хотя бы одну большую букву и не менее трёх цифр. 
# Тогда он будет считаться надёжным. 

# Напишите программу, которая просит пользователя придумать пароль 
# до тех пор, пока этот пароль не станет надёжным. 
# Должна использоваться латиница.

# Пример
# Придумайте пароль: qwerty.
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty12.
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty123.
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qWErty123.
# Это надёжный пароль.

def pass_strength(password):
    count = 0
    if len(password) < 8:
        print('Длина менее 8 символов. ', end='')
        return True
    elif password.islower() or password.isupper():
        print('Нужен верхний и нижний регистр. ', end='')
        return True
    elif password.isalpha() or password.isdigit():
        print('Нужны цифры и буквы. ', end='')
        return True
    else: 
        for i in list(password):
            if i.isdigit():
                count += 1
        if count < 3:
            print('Нужно не менее трёх цифр.', end='')
            return True


my_password = input('Придумайте пароль: ')

while pass_strength(my_password):
    print('Пароль ненадёжный. Попробуйте ещё раз.')
    my_password = input('Придумайте пароль: ')

print('Это надёжный пароль.')


# ну нагородил )))))
# не получается у меня Pythonic )))))
# как научиться?

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:

    password = input('Придумайте пароль: ')
    upper_count = 0
    num_count = 0
    for i_sym in password:

        if i_sym in alphabet:
            if i_sym.isupper():
                upper_count += 1

        elif '0' < i_sym < '9':
            num_count += 1

    if len(password) < 8 or upper_count < 1 or num_count < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')

    else:
        print('Это надёжный пароль!')
        break