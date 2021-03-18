# Задание 5

# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import os
from random import randint

MAX_RANDOM_NUMBERS = 10000
MAX_RANDOM_VALUE = 100
file_name = os.path.join('data', 'file_5_5.txt')

with open(file_name, 'w') as f_out:
    num_of_numbers = randint(1, MAX_RANDOM_NUMBERS)
    print(f'Generating: {num_of_numbers} random numbers')
    random_numbers = [str(randint(1, MAX_RANDOM_VALUE)) for _ in range(num_of_numbers)]
    f_out.write(' '.join(random_numbers))

with open(file_name) as f_in:
    numbers = f_in.read()
    print(f"Sum of numbers is: {sum([int(number) for number in numbers.split()])}")