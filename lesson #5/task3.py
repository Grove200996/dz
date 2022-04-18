from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена','Stan','DickStasy','Brax','Summit1g'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


my_list = (i for i in zip_longest(tutors, klasses))
print(type(my_list))
print(*my_list, sep=('\n'))

######################

def dictionary(tutor,klass):
    for i in range(len(tutor)):
        yield tutor[i],klass[i] if i < len(klasses) else None

print(*dictionary(tutors,klasses), sep='\n')