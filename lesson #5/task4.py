# 4. Представлен список чисел. Необходимо вывести те его элементы,
#     значения которых больше предыдущего.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
r = []
for i in range(len(src)-1):
    if src[i] < src[i+1]:
        r.append(src[i+1])

print(r)

res = [j for i, j in zip(src, src[1:]) if j > i]
print(*zip(src,src[1:]))
# i == src[0]
# j == src[1:][0]

print(res)