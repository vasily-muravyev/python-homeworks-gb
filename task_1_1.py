# Задание 1

# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

# взял фрагмента кода из последнего дз по курсу ml-intro от Rolling Scopes, который прохожу сейчас

# 1.1. Работа с числами.
# Вычисление Information Gain для двух разных разбиений для задачи классификации при помощи дерева решений
# Исходное разбиение на классы (9, 11). Два новых возможных подразбиения (5, 8) + (6, 1) и (2, 7) и (9, 2)

import numpy as np

parent_node_entropy = -11/20 * np.log2(11/20) - 9/20 * np.log2(9/20)
print(parent_node_entropy)

first_split_entropy = 13/20 * (-5/13 * np.log2(5/13) - 8/13 * np.log2(8/13)) + \
                      7/20 * (-6/7 * np.log2(6/7) - 1/7 * np.log2(1/7))
print(first_split_entropy, parent_node_entropy - first_split_entropy)


second_split_entropy = 9/20 * (-2/9 * np.log2(2/9) - 7/9 * np.log2(7/9)) + \
                      11/20 * (-9/11 * np.log2(9/11) - 2/11 * np.log2(2/11))
print(second_split_entropy, parent_node_entropy - second_split_entropy)

# 1.2. Работа со строками - пользовательский ввод

your_name = input('Hey! How what\'s your_name?: >>> ')
sleep_time = int(input("How many hours of sleep do you need to feel yourself well?: >>> "))

print(f"Name: {your_name}. Hours of sleep needed: {sleep_time}")