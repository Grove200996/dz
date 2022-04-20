class Cell:
    def __init__(self, size):
        # кол-во клеток
        self.size = size
    def __str__(self):
        return str(self.size)

    def __add__(self, other):
        return self.size + other.size

    def __sub__(self, other):
        return self.size - other.size

    def __mul__(self, other):
        return self.size * other.size

    def __floordiv__(self, other):
        return self.size / other.size

cell_1 = Cell(2)
cell_2 = Cell(3)
print(cell_2 + cell_1)
print(cell_2 - cell_1)
print(cell_2 // cell_1)
print(cell_2 * cell_1)