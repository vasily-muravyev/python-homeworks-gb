# Задание 3.

# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season_list = [None,  # 0
               'Winter',  # 1
               'Winter',  # 2
               'Spring',  # 3
               'Spring',  # 4
               'Spring',  # 5
               'Summer',  # 6
               'Summer',  # 7
               'Summer',  # 8
               'Autumn',  # 9
               'Autumn',  # 10
               'Autumn',  # 11
               'Winter']  # 12

season_dict = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter'}

month_number = int(input('Enter month number >>> '))
print(f"season by list: {season_list[month_number]}\nseason by dict: {season_dict[month_number]}")
