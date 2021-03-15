# Задание 5

# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()

from functools import reduce

answer1 = reduce(lambda x, y: x * y, [number for number in range(100, 1001, 2)])

answer2 = 1
for i in range(100, 1001, 2):
    answer2 *= i

assert(answer1 == answer2)
print(answer1)
