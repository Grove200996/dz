class Road():
    def __init__(self, lenght, widht):
        self.__lenght = lenght
        self.__widht = widht

    def calculation(self):
        mass = self.__widht * self.__lenght * 25 * 5
        return mass
a = Road(20,5000)
print(a.calculation())
