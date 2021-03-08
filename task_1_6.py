# Задание 6

# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня

# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

initial_kms = float(input('Enter initial amount of km\'s: '))
desired_kms = float(input('Enter desired amount of km\'s: '))

current_kms = initial_kms
day = 12

while current_kms < desired_kms:
    print(f'day {day} result is {round(current_kms, 1)} km')
    current_kms = current_kms * 1.1
    day += 1

print(f'Congrats! On day {day} you have achieved you target. Result is {round(current_kms, 1)} km! Keep on running!')