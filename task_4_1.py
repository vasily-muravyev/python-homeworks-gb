# Задание 1

# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys


def calculate_salary(hours, payment_per_hour, bonus):
    return hours * payment_per_hour + bonus


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: task_4_1.py hours payment_per_hour bonus')
    else:
        hours_, payment_per_hour_, bonus_ = [int(arg) for arg in sys.argv[1:]]
        print(calculate_salary(hours_, payment_per_hour_, bonus_))