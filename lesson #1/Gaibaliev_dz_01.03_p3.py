# Задача 3
number = int(input('Введите число: '))
if number % 10 == 1 and not number // 10 == 1:
    print(f'{number} процент')
elif 2 <= number % 10 <= 4:
    print(f'{number} процента')
elif number % 10 >= 5:
    print(f'{number} процентов')
else:
    print(f'{number} процентов')
