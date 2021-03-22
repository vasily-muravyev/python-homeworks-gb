# Задание 3

# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self._name  = name
        self._surname = surname
        self._position = position
        self._income = {'wage' : wage, 'bonus': bonus}

    def get_position(self):
        return self._position


class Position(Worker):

    def get_full_name(self):
        return self._surname + " " + self._name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position1 = Position('Ivan', 'Petrov', 'Data Engineer', 30000, 5000)
position2 = Position('Vasily', 'Sidorov', 'CEO', 50000, 2000)

for position in [position1, position2]:
    print(f"{position.get_full_name()} ({position.get_position()}) with total income {position.get_total_income()}")