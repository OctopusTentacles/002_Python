print('1 - км/ч в м/с')
print('2 - м/с в км/ч')
wind = int(input())

if wind == 1:
    km = float(input('км/ч = '))
    ms = km * 1000 / 3600
    print('м/с =', round(ms, 2))
elif wind == 2:
    ms = float(input('м/с = '))
    km = ms * (1/1000) / (1 / 3600)
    print('км/ч', round(km, 2))


if 10.8 <= ms <= 13.8:
    print('Ветер сильный, 6 баллов, Качаются толстые сучья деревьев, гудят телеграфные провода.')


