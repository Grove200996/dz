# 5. Реализовать функцию get_jokes(),
# возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_joke(num):
    """
    Joke generator, nothing else to say.
    :param num: enter a number of jokes you want to generate.
    :return: it's gonna return three random words in a list 'num' times.

    """
    joke = []
    for i in range(num):
        joke.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return joke
