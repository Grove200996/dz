# Задача № 2.
my_list = [i ** 3 for i in range(1, 1000, 2)]
print(my_list)
summ = 0
for number in my_list:
    number_2 = str(number)
    digits_summ = 0
    for inner_number in number_2:
        digits_summ += int(inner_number)
    if digits_summ % 7 == 0:
        summ += number
print(summ)
