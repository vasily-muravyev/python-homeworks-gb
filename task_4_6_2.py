# Задание 6. Часть 2

# Описание см в части 1

import sys
from itertools import cycle

my_action_list = ['python', 'machine learning', 'data engineering', 'eat', 'sleep']

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: task_4_6_2.py cycles_count")
    else:
        cycles = int(sys.argv[1])
        for index, action in enumerate(cycle(my_action_list), 1):
            print(action)
            if index == cycles * len(my_action_list):
                break
