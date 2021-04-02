"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import numpy as np


class LottoCard:
    def __init__(self, player_name):
        self.player_name = player_name
        self.card, self.card_spaces = LottoCard.generate_random_card()
        self.crossed_numbers = set()

    def __str__(self):
        header = '-' * 15 + ' ' + self.player_name + ' ' + '-' * 15 + '\n';
        rows = ''
        for i in range(3):
            one_line = ''
            row_spaces = set(self.card_spaces[i])
            row_values = iter(self.card[i])
            for j in range(9):
                if j in row_spaces:
                    one_line += '   '
                else:
                    next_value = next(row_values)
                    one_line += str(next_value if next_value not in self.crossed_numbers else '-') + '  '
            rows += one_line + '\n'
        return header + rows + '-' * (32 + len(self.player_name)) + '\n'

    @staticmethod
    def generate_random_card():
        """generates random lotto card and spaces"""
        return np.sort((np.random.permutation(90) + 1)[:15].reshape(3, -1)), \
               np.sort(np.array([np.random.permutation(9)[:4] for i in range(3)]))

    @property
    def all_crossed(self):
        return len(self.crossed_numbers) == 15

    def cross_number(self, number):
        """
        crosses number if exists
        :return True if there was number on a card and False otherwise
        """
        for i in range(3):
            for j in range(5):
                if self.card[i, j] == number:
                    self.crossed_numbers.add(number)
                    return True
        return False

    def has_number_on_card(self, number):
        """
        checks if number exists on card
        :return True if there is number and it's not crossed and False otherwise
        """
        for i in range(3):
            for j in range(5):
                if self.card[i, j] == number and number not in self.crossed_numbers:
                    return True
        return False


class LottoGame:

    def __init__(self):
        self.player_card = LottoCard('Игрок')
        self.computer_card = LottoCard('Компьютер')

    @staticmethod
    def __get_next_number():
        random_numbers = np.random.permutation(90) + 1
        for i, number in enumerate(random_numbers, 1):
            yield i, number

    def play(self):
        for i, number in self.__get_next_number():
            print(f"Новый бочонок: {number} (осталось {90 - i})", '\n')
            print(self.player_card)
            print(self.computer_card)
            choice = input("Зачеркнуть цифру? (y / n) ")
            if choice == 'y':
                loss = not self.player_card.cross_number(number)
            else:
                loss = self.player_card.has_number_on_card(number)
            if loss:
                print("Игрок проиграл...")
                break
            elif self.player_card.all_crossed:
                print("Игрок выиграл!")
                break
            elif self.player_card.all_crossed:
                print("Компьютер выиграл!")
                break

            # just cross number for computer - it's always correct in this version of program
            if self.computer_card.has_number_on_card(number):
                self.computer_card.cross_number(number)


game = LottoGame()
game.play()