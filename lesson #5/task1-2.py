# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

def odd(num):
    for i in range(num + 2):
        if i > num:
            yield f'StopIteration'
        elif i % 2 != 0:
            yield i



a = odd(15)
print(type(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))






###############


# 2 Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

nums = (i for i in range(1, 15 + 1, 2))
print(next((nums)))
print(next((nums)))

nums_list = [i for i in range(1, 15 + 1, 2)]
print(nums_list)
