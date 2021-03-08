# Задание 4

# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

number = int(input("Enter positive integer number:\n>>> "))

max_digit = 0
while number != 0:
    digit = number % 10
    max_digit = digit if digit > max_digit else max_digit
    number = number // 10

print(f"max digit: {max_digit}")