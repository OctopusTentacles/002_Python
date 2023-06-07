# Задача 3. Пакеты

# При работе с сервером мы кодируем сообщение и отправляем его в виде пакетов информации. 
# Их количество равно N. Допустим, каждый пакет содержит четыре числа, 
# каждое из которых равно нулю или единице. Эти числа называются битами. 
# Иногда в кодировке сообщения встречаются ошибки, и в пакете эта ошибка 
# обозначается числом -1. Если таких ошибок не больше одной, то этот пакет мы 
# целиком добавляем в список для декодирования, а иначе отбрасываем.

# Напишите программу, которая будет обрабатывать полученные пакеты и выведет 
# на экран итоговое сообщение для декодирования, а также количество ошибок 
# в нём и количество необработанных пакетов.

# Пример:
# Кол-во пакетов: 3

# Пакет номер 1
# 1 бит: 1
# 2 бит: 0
# 3 бит: -1
# 4 бит: 1

# Пакет номер 2
# 1 бит: -1
# 2 бит: -1
# 3 бит: 1
# 4 бит: 1
# Много ошибок в пакете.

# Пакет номер 3
# 1 бит: 0
# 2 бит: 1
# 3 бит: 1
# 4 бит: 1

# Полученное сообщение: [1, 0, -1, 1, 0, 1, 1, 1]
# Кол-во ошибок в сообщении: 1
# Кол-во потерянных пакетов: 1


decode = []
bad_packs = 0

packs_amt = int(input('Кол-во пакетов: '))

for i in range(packs_amt):
    pack = []
    print('\nПакет номер', i + 1)
    for i_bit in range(4):
        bit = int(input(f'{i_bit + 1} бит: '))
        pack.append(bit)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Много ошибок в пакете.')
        bad_packs += 1

print('\nПолученное сообщение:', decode)
print('Кол-во ошибок в сообщении:', decode.count(-1))
print('Кол-во потерянных пакетов:', bad_packs)