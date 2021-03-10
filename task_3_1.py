# Задание 1

# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def quotient(dividend, divider):
    try:
        return dividend / divider
    except ZeroDivisionError:
        return None


my_dividend = int(input('Enter dividend: '))
my_divider = int(input('Enter divider: '))

my_quotient = quotient(my_dividend, my_divider)
print(f"{my_dividend} / {my_divider} = {my_quotient}")