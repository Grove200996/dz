import time
from itertools import cycle

# Класс
# class TraficLight():
#     # Атрибуты светофора
#     def __init__(self):
#         self._color = ['red','yellow','green']
#
#     # Методы светофора
#     def running(self):
#         print(a._color[0])
#         time.sleep(7)
#         print(a._color[1])
#         time.sleep(2)
#         print(a._color[2])
#         time.sleep(5)
#         print(a._color[0])
#
#
# a = TraficLight()
# a.running()
######################3


class TraficLight():
    # Атрибуты светофора
    def __init__(self):
        self._color = (('red',7),('yellow',2),('green',5))

    # Методы светофора
    def running(self):
        for color,sec in cycle(self._color):
            print(color)
            time.sleep(sec)
a = TraficLight()
a.running()