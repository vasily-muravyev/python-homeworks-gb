# Задание 3

# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def sum_of_two_largest(num1, num2, num3):
    return sum([num1, num2, num3]) - min(num1, num2, num3)


print(sum_of_two_largest(1, 2, 3))
print(sum_of_two_largest(3, 2, 6))