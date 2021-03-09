# Задание 5.

# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating_list = [9, 9, 7, 5, 3, 3, 2]

print(f"Initial rating: {rating_list}")
print('Adding new elements to rating. To quit enter "q"')
while True:
    new_number = input('Enter new element of rating >>> ')
    if new_number == 'q':
        break
    new_number = int(new_number)

    # we could use binary search here if we needed more efficient solution
    length_of_list = len(rating_list)

    # if new element is smallest just append to the end
    if new_number < rating_list[length_of_list - 1]:
        rating_list.append(new_number)
    # else look for first element in rating that is smaller than new
    else:
        for i in range(length_of_list):
            if new_number > rating_list[i]:
                rating_list.insert(i, new_number)
                break

    print(f"Rating after update: {rating_list}")