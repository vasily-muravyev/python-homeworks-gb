# Задание 2

# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []

print("Add elements to list, to finish enter 'q'")
while True:
    elem = input(">>> ")
    if elem == 'q':
        break
    else:
        my_list.append(elem)

print(f"original list: {my_list}")

for pair_index in range(len(my_list) // 2):
    my_list[pair_index * 2], my_list[pair_index * 2 + 1] = my_list[pair_index * 2 + 1], my_list[pair_index * 2]

print(f"list after swap: {my_list}")