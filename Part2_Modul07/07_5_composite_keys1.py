# Задача 1. Паспортные данные
# В базе данных поликлиники хранятся паспортные данные людей. 
# Хранение реализовано с помощью словаря, состоящего из пар «Серия и номер паспорта — 
# фамилия и имя». Серия и номер — составной ключ, а фамилия и имя — составное значение.

# Реализуйте функцию, которая по номеру и серии паспорта выдаёт имя и фамилию человека.


data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

serial = int(input('введите сирию паспорта: '))
number = int(input('введите номер паспорта: '))

serial_number = (serial, number)

if serial_number in data:
    print(data[serial_number])
else:
    print("Такого человека нет")