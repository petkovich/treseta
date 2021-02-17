from game import *
from player import Player
import itertools
import numpy as np


class Treseta:
    def __init__(self):
        self.points = [0, 0]
        self.cards = None
        self.p1 = None
        self.p2 = None
        self.played_cards = []
        self.hands_played = 0
        self.next_player = 0
        self.new_game()

    def new_game(self):
        self.points = [0, 0]
        self.hands_played = 0
        self.next_player = 0
        cards = np.arange(40)
        np.random.shuffle(cards)
        self.cards = cards
        self.p1 = Player(self.cards[0:10])
        self.p2 = Player(self.cards[10:20])
        self.played_cards = []

        # self.play_game()

    def play_game(self, verbose=True):
        while self.hands_played < 20:  # 20
            if verbose:
                print_hand(self.p1.get_hand())
                print_hand(self.p2.get_hand())
                print(self.next_player)

            if self.next_player == 0:
                first_card = self.p1.play_card()
                self.p2.he_played(first_card)
                second_card = self.p2.play_card(first_card)
                self.p1.he_played(second_card)
                second_won = stronger_card(first_card, second_card)
                if not second_won:  # first player won
                    self.points[0] += (
                        points[get_number(first_card)] + points[get_number(second_card)]
                    )
                else:
                    self.points[1] += (
                        points[get_number(first_card)] + points[get_number(second_card)]
                    )
                    self.next_player = 1
            else:
                first_card = self.p2.play_card()
                self.p1.he_played(first_card)
                second_card = self.p1.play_card(first_card)
                self.p2.he_played(second_card)
                second_won = stronger_card(first_card, second_card)
                if not second_won:  # second player won
                    self.points[1] += (
                        points[get_number(first_card)] + points[get_number(second_card)]
                    )
                else:
                    self.points[0] += (
                        points[get_number(first_card)] + points[get_number(second_card)]
                    )
                    self.next_player = 0
            if verbose:
                print_card(first_card)
                print_card(second_card)
                print(self.points)
            if self.hands_played < 10:
                first_draw = self.cards[20 + self.hands_played * 2]
                second_draw = self.cards[20 + self.hands_played * 2 + 1]
                if verbose:
                    print_card(first_draw)
                    print_card(second_draw)
                if self.next_player == 0:
                    self.p1.get_card(first_draw)
                    self.p2.opponent_got(first_draw)
                    self.p2.get_card(second_draw)
                    self.p1.opponent_got(second_draw)

                else:
                    self.p2.get_card(first_draw)
                    self.p1.opponent_got(first_draw)
                    self.p1.get_card(second_draw)
                    self.p2.opponent_got(second_draw)

            self.hands_played += 1

        self.points[self.next_player] += last_hand_point
        return self.points

    def play_n_games(self, n):
        total_result = [0, 0]
        for i in range(n):
            self.new_game()
            current_result = self.play_game()
            total_result[0] += math.floor(current_result[0] / 3)
            total_result[1] += math.floor(current_result[1] / 3)
        print(total_result)
        print(total_result[0] / sum(total_result), total_result[1] / sum(total_result))


treseta = Treseta()
treseta.play_n_games(1)
