# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
workers = ['инженер-конструктор Игорь','главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# first_name = workers[0].title().split()
# second_name = workers[1].title().split()
# third_name = workers[2].title().split()
# fourth_name = workers[3].title().split()
# print(f'Привет, {first_name[-1]}')
# print(f'Привет, {second_name[-1]}')
# print(f'Привет, {third_name[-1]}')
# print(f'Привет, {fourth_name[-1]}')


for i in range(len(workers)):
    workers[i] = workers[i].split()
    print(f'Привет, {workers[i][-1].title()}')