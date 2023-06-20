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
    if len(password) < 8:
        print('Длина менее 8 символов. ', end='')
        return True
    elif password.islower() or password.isupper():
        print('Нужен верхний и нижний регистр. ', end='')
        return True
    elif password.isalpha() or password.isdigit():
        print('Нет цифр. ', end='')
        return True

my_password = input('Придумайте пароль: ')

while pass_strength(my_password):
    print('Пароль ненадёжный. Попробуйте ещё раз.')
    my_password = input('Придумайте пароль: ')

print('Это надёжный пароль.')