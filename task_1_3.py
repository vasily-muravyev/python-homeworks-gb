# Задание 3

# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# воспользуемся тем свойством что строки можно умножать для дублирования

number = input('Please enter number:\n>>> ')
sum_of_numbers = int(number) + int(number * 2) + int(number * 3)
print(f"sum: {sum_of_numbers}")