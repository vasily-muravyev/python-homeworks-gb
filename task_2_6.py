# Задание 6
#
# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

products = []
index_of_last_product = 0
print('Adding new products. To quit enter "q"')

while True:
    new_product = input('Enter separated by spaces product data:\n(name price amount units) >>> ')
    if new_product == 'q':
        break
    name, price, amount, units = new_product.split()
    index_of_last_product += 1
    products.append((index_of_last_product,
                     {'name': name,
                      'price': price,
                      'amount': amount,
                      'units': units}))

print('Original structure:')
print(products, '\n')

analytic = {}
for index, product in products:
    for key, value in product.items():
        # we could use default dict structure here to avoid this check
        if key in analytic:
            analytic[key].append(value)
        else:
            analytic[key] = [value]

print('Analytic data:')
print(analytic)

