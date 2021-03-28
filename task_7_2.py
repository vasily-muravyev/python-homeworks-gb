# Задание 2

# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self._size = size

    def tissue_consumption(self):
        return (self._size / 6.5) + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self._height = height

    def tissue_consumption(self):
        return 2 * self._height + 0.3


class ClothesManufacture:

    def __init__(self):
        self.__clothes = []

    def produce_clothes(self, *args):
        self.__clothes.extend(args)

    @property
    def total_tissue_consumption(self):
        return sum([clothes.tissue_consumption() for clothes in self.__clothes])


coat = Coat(11)
another_coat = Coat(12)
costume = Costume(20)

print(coat.tissue_consumption(), 11 / 6.5 + 0.5)
print(costume.tissue_consumption(), 2 * 20 + 0.3)
print(another_coat.tissue_consumption(), 12 / 6.5 + 0.5)


manufacture = ClothesManufacture()
manufacture.produce_clothes(coat, costume, another_coat)
print(f"Total tissue consumption: {manufacture.total_tissue_consumption}")
print(f"Total tissue consumption (check manually): "
      f"{coat.tissue_consumption() +another_coat.tissue_consumption() + costume.tissue_consumption()}")