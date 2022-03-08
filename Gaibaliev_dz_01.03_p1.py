# Задача №1.
number = int(input("Введите число: "))
sec = number % 60
min = number // 60 % 60
hour = number // 3600 % 24
day = number // 86400

if day < 1 and hour < 1 and min < 1:
    print(f'{sec} сек.')
if day < 1 and hour < 1 and min >= 1:
    print(f'{min} мин. {sec} сек.')
if day < 1 and hour >= 1 and min > 0:
    print(f'{hour} час. {min} мин. {sec} сек.')
if day >= 1 and hour >= 1 and min >= 0:
    print(f'{day} д. {hour} час. {min} мин. {sec} сек.')



