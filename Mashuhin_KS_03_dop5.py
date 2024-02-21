'''
Krazy King BlackJack is just like blackjack, with one difference: the kings! Instead of the kings being simply worth 10 points, kings are worth either 10 points or some other number of points announced by the dealer at the start of the game. Whichever value yields the best hand is the one that plays (much like how aces are worth either 1 or 11 points).

Write a function that inputs a list of strings (representing a blackjack hand) and an integer that represents the alternative king value. The function should output an integer representing the value of the hand if it is less than or equal to 21, and False if it exceeds 21. Other than the alternative king value, normal blackjack rules apply.

The cards, in order ace-through king, are represented as strings as follows:

['A', '2', '3','4', '5', '6','7', '8', '9','10', 'J', 'Q','K']
A hand has between 2 and 20 cards, inclusive. The alternative king value is between 2 and 9, inclusive.

Blackjack rules: the value of a hand is determined by maximizing the value of the sum of its cards while not exceeding 21 if possible. Number cards are worth their value, Jacks ('J') and Queens ('Q') are worth 10, Aces are worth either 1 or 11, and kings, again, are worth either 10 or their alternative value.
'''


def calculate_hand_value(hand, alt_king_value):
    # Словарь для перевода карт в их числовое значение
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    total = 0
    aces = 0  # Количество тузов
    # Переводим карты в числовые значения и считаем тузы
    for card in hand:
        if card == 'A':
            aces += 1
        elif card == 'K':
            # Добавляем альтернативное значение короля или 10, в зависимости от того, что лучше
            total += min(alt_king_value, 10) if total + \
                min(alt_king_value, 10) > 21 else min(alt_king_value, 10)
        else:
            total += values[card]
    for i in range(aces):     # Максимизируем значение тузов, пока сумма не превышает 21
        if total + 11 > 21:
            total += 1  # Используем туза как 1
        else:
            total += 11  # Используем туза как 11
    if total > 21:
        return False
    else:
        return total


print(calculate_hand_value(str(input("Введите комбинацию карт: ")),
      int(input("Введите размер короля: "))))
