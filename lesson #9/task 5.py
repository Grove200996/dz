class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'ручка рисует'


class Pencil(Stationery):
    def draw(self):
        return f'карандаш рисует'


class Brush(Stationery):
    def draw(self):
        return f'кисть рисует'

a = Pencil('карандаш')
b = Brush('кисть')
c = Pen('ручка')
print(a.draw())
print(b.draw())
print(c.draw())

