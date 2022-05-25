
duration = int(input('Введите количество секунд: '))

second = duration % 60
minute = duration // 60
hour = minute // 60
day = hour // 24


if duration < 0:
    print('Вы ввели отрицательное число')
elif minute == 0:
    print(second, 'сек')
elif hour == 0:
    print(minute, 'мин', second, 'сек')
elif day == 0:
    print(hour, 'час', minute - hour * 60, 'мин', second, 'сек')
else:
    print(day, 'дн', hour - day * 24, 'час', minute - hour * 60, 'мин', second, 'сек')
