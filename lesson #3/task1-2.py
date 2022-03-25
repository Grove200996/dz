# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c русского на английский язык.


dictionary = {'один': 'one',
              'два': 'two',
              'три': 'three',
              'четыре': 'four',
              'пять': 'five',
              'шесть': 'six',
              'семь': 'seven',
              'восемь': 'eight',
              'девять': 'nine',
              'десять': 'ten'}


def translator_adv(num):
    if num == num.lower():
        return dictionary.get(num)
    if num == num.capitalize():
        num = num.lower()
        lower = dictionary[num]
        return lower.capitalize()


print(translator_adv('Шесть'))