# Задание 3

# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

import os

with open(os.path.join('data', 'file_5_3.txt')) as f:
    sum_of_salaries = 0
    num_of_employees = 0
    for line in f:
        family, salary = line.split()
        salary = float(salary)
        sum_of_salaries += salary
        num_of_employees += 1
        if salary >= 20000:
            print(f"Family: {family}, salary: {salary}")
    print(f"Average salary: {sum_of_salaries / num_of_employees}")
