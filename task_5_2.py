# Задание 2

# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

import os

with open(os.path.join('data', 'file_5_2.txt')) as f:
    for index, line in enumerate(f, start=1):
        print(f"line #{index}: words: {len(line.split())}")
    else:
        print(f"Total lines: {index}")