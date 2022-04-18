class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} поворачивает на{direction}'

    def show_speed(self):
        return f'текущая скорость {self.speed}  км/ч'


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            return f'слишком большая скорость'
class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            return f'сбавьте скорость'
class SportCar(Car):
    pass

class PoliceCar(Car):
    pass


town_car = TownCar(160,'чёрный','solaris',False)
work_car = WorkCar(140,'белый','traffic',False)
sport_car = SportCar(220,'жёлтый','supra',False)
police = PoliceCar(10,'сине-белый','велосипед', True)

print(town_car.name)
print(town_car.speed)
print(town_car.show_speed())
