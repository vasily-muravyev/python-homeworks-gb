# Задание 4.

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4

# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import os

translations = {
    'One' : 'Один',
    'Two' : 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open(os.path.join('data', 'file_5_4.txt'), encoding='utf8') as f_in:
    with open(os.path.join('data', 'file_5_4_translated.txt'), 'w', encoding='utf8') as f_out:
        for line in f_in:
            words = line.split()
            words[0] = translations[words[0]]
            f_out.write(' '.join(words) + '\n')

