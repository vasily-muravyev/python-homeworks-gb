# Задание 4.

# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed: int, color: str, name: str):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = False

    def go(self):
        print(f'{self._name}. Go!')

    def stop(self):
        print(f'{self._name}. Stopped.')

    def turn(self, direction : str):
        print(f"{self._name}. Turn to the {direction}")

    def show_speed(self):
        print(f"{self._name}. Current speed is {self._speed}")

    def is_police(self):
        return self._is_police

    def info(self):
        print(f"{self._name},"
              f" speed: {self._speed},"
              f" color: {self._color},"
              f" is_police: {self._is_police}")


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print(f'TownCar speed is over the Town limit (60 km per hour)')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print(f'WorkCar speed is over the limit (40 km per hour)')


class PoliceCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self._is_police = True


cars = [TownCar(speed=30, color='red', name='VW Polo'),
        TownCar(speed=80, color='blue', name='Toyota'),
        SportCar(speed=140, color='white', name='Lamborghini'),
        PoliceCar(speed=70, color='yellow', name='Audi'),
        WorkCar(speed=80, color='green', name='Nissan'),
        WorkCar(speed=20, color='orange', name='Chevrolet')]

for car in cars:
    car.info()
    car.show_speed()
    print()

cars[1].go()
cars[1].turn('right')
cars[1].turn('left')
cars[1].stop()


