# Задание 7.

# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.

import os
import numpy as np
import json

input_file_name = os.path.join('data', 'file_5_7.txt')
json_file_name = os.path.join('data', 'file_5_7.json')

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

firm_income = {}

with open(input_file_name, encoding='utf8') as f:

    for line in f:
        name, firm_type, income, losses = line.split()
        profit, losses = float(income), float(losses)
        income = profit - losses
        print(f'Income of {name}: {income}')
        firm_income[name] = income

    mean_income = np.mean([income for income in firm_income.values() if income > 0])
    print(f"Mean income of profitable firms: {mean_income:.3f}")

# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

firm_data = [firm_income, {'average_profit' : round(mean_income, 3)}]

# Итоговый список сохранить в виде json-объекта в соответствующий файл.

# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджеры контекста.

with open(json_file_name, 'w', encoding='utf8') as f:
    json.dump(firm_data, f)

with open(json_file_name, 'r', encoding='utf8') as f:
    firm_data_restored = json.load(f)

assert(firm_data == firm_data_restored)




