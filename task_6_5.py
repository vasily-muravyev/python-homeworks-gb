# Задание 5

# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title: str):
        self._title = title

    def draw(self):
        print(f'{self._title}. Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'{self._title}. Запуск отрисовки ручки.')


class Pencil(Stationery):

    def draw(self):
        print(f'{self._title}. Запуск отрисовки карандаша.')


class Handle(Stationery):

    def draw(self):
        print(f'{self._title}. Запуск отрисовки маркера.')


objects = [Stationery('Мелок'),
           Pen('Parker'),
           Pencil('Koh-i-Noor'),
           Handle('Attache')]

for obj in objects:
    obj.draw()