# Задание 5

# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def accumulate_user_input():
    accumulated_sum = 0
    print('Accumulating numbers from user input. To cancel press "q"')

    while True:
        sentence_of_numbers = input('Separated by space numbers >>> ')
        for num in sentence_of_numbers.split():
            if num == 'q':
                return accumulated_sum
            else:
                accumulated_sum += float(num)
        print(f'Current sum is: {accumulated_sum}')


print(f'Final sum is: {accumulate_user_input()}')