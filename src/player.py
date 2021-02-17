from game import *
import math
import numpy as np
import random


class Player:
    def __init__(self, cards):
        self.hand = sorted(cards)
        self.round = 0
        self.opponent_draw = []
        self.played_cards = []
        # print_hand(self.hand)

    def get_hand(self):
        return self.hand

    def play_card(self, played_card=None):
        if played_card is not None:
            options = legal_options(self.hand, played_card)
        else:
            options = self.hand

        if len(options) == 1:
            played_card = options[0]
        else:
            played_card = self.select_best_option(options)
        self.played_cards.append(played_card)
        self.hand.remove(played_card)
        return played_card

    def select_best_option(self, options):
        return random.choice(options)

    def get_card(self, card):
        self.hand.append(card)
        self.hand = sorted(self.hand)

    def opponent_got(self, card):
        self.opponent_draw.append(card)

    def he_played(self, card):
        self.played_cards.append(card)
