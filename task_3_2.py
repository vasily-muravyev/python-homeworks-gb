# Задание 2

# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def print_user_data(name, family, year_of_birth, city, email, phone):
    print(f"name: {name}\n"
          f"family: {family}\n"
          f"year of birth: {year_of_birth}\n"
          f"city: {city}\n"
          f"email: {email}\n"
          f"phone: {phone}")


print_user_data(name='Vasily',
                family='Muravyev',
                phone='911',
                email='mymail@mail.ru',
                year_of_birth=1986,
                city='Moscow')