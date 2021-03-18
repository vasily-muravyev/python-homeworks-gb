# Задание 1

# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

import os

with open(os.path.join('data', 'file_5_1.txt'), 'w') as f:
    while True:
        line = input(">>> ")
        if len(line) == 0:
            break
        else:
            f.write(line + '\n')
