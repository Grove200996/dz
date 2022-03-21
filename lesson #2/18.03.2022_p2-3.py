# 2. Дан список:
my_list = ['в', '5', 'часов', '17', 'минут', 'температура',
           'воздуха', 'была', '+5', 'градусов']


def things(x):
    if x[0] in '+-':
        return x[0]



i = 0
while i < len(my_list):
    addition = things(my_list[i])
    if my_list[i].isdigit() or (addition and my_list[i][1:].isdigit()):
        if addition:
            my_list[i] = addition + my_list[i][1:].zfill(2)
        else:
            my_list[i] = my_list[i].zfill(2)
        my_list.insert(i, '"')
        my_list.insert(i + 2, '"')
        i += 2
    i += 1
print(' '.join(my_list))
######################
string = ''
for i in my_list:
    things = '"'
    if i == things:
        string += '' + i + ''
    elif i.isdigit() or i.startswith('+'):
        string += i
    else:
        string += ' ' + i + ' '
print(string.strip())
