colors = ["spade", "dinare", "kupe", "bastoni"]
numbers = [
    "cetvorka",
    "petica",
    "sestica",
    "sedmica",
    "fanat",
    "kaval",
    "kralj",
    "as",
    "duja",
    "trica",
]
points = [0, 0, 0, 0, 1, 1, 1, 3, 1, 1]  # it's /3 actually
points_dict = {}
for i in range(len(numbers)):
    points_dict[numbers[i]] = points[i]
last_hand_point = 3

import math


def get_color(card):
    return int(math.floor(card / 10))


def get_number(card):
    return card % 10


def stronger_card(first_card, second_card):
    same_color = get_color(first_card) == get_color(second_card)
    if same_color:
        return int(second_card > first_card)
    return 0


def print_card(x):
    if x is not None:
        print(f"{numbers[x % 10]}  {colors[get_color(x)]}")
    else:
        print(x)


def print_hand(cards):
    string_cards = [f"{numbers[x % 10]}  {colors[get_color(x)]}" for x in cards]
    print(string_cards)


def legal_options(hand, played_card):
    legal_cards = [x for x in hand if get_color(played_card) == get_color(x)]
    if len(legal_cards):
        return legal_cards
    else:
        return hand
