# Задание 1.

# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

# я чуть-чуть усложнил задачу позволив задавать начальный свет цветофора не обязательно красным

from itertools import cycle, chain
import time


class TrafficLight:

    __lights = ['red', 'yellow', 'green']
    __color_to_time = {'red' : 7, 'yellow' : 2, 'green' : 3}

    def __init__(self, color):
        assert color in TrafficLight.__lights, "only red, yellow, green colors are allowed"
        self.__color = color

    def running(self):
        index_of_first_color = TrafficLight.__lights.index(self.__color)
        first_colors = TrafficLight.__lights[index_of_first_color:]
        for color in chain(first_colors, cycle(TrafficLight.__lights)):
            self.__color = color
            print(f'current color: {self.__color}')
            time.sleep(TrafficLight.__color_to_time[self.__color])


traffic_light = TrafficLight('green')
traffic_light.running()