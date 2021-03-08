# Задание 5

# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


profit = int(input('Enter company profit: '))
costs = int(input('Enter company costs: '))

is_profitable = profit > costs

if is_profitable:
    revenue = profit - costs
    print(f'Company is profitable. Revenue is {revenue}')
    employees_count = int(input('Enter employees count: '))
    print(f'Revenue per employee is {round(revenue / employees_count, 3)}')
else:
    print("Company is not profitable. You'd better do something else!")