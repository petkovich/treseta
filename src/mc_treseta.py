from abc import ABC, abstractmethod
from mctspy.games.common import TwoPlayersAbstractGameState, AbstractGameAction
from game import *

import math
import random


class PlayCard(AbstractGameAction):
    def __init__(self, card):
        self.card = card

    def __repr__(self):
        return f"Played {self.card}"


class Treseta(ABC):
    def __init__(
        self,
        points,
        p1_hand,
        p2_hand,
        # p1_knowledge=[],
        # p2_knowledge=[],
        played_cards=[],
        played_card=None,
        next_to_move=0,
    ):
        self.points = points
        self.p1_hand = p1_hand
        self.p2_hand = p2_hand
        self.played_cards = played_cards
        self.played_card = played_card
        self.next_to_move = next_to_move
        self.remaining_cards = [
            x
            for x in range(40)
            if x not in played_cards and x not in p1_hand and x not in p2_hand
        ]
        random.shuffle(self.remaining_cards)

    @property
    def game_result(self):
        """
        this property should return:
         1 if player #1 wins
        -1 if player #2 wins
         0 if there is a draw
         None if result is unknown
        Returns
        -------
        int
        """
        # print(len(self.played_cards))
        if len(self.played_cards) == 40:
            return 0
            self.points[self.next_to_move] += last_hand_point
            # return math.floor(self.points[1] / 3)
            if self.points[1] > self.points[0]:
                return 1
            else:
                return -1
        return None

    def is_game_over(self):
        """
        boolean indicating if the game is over,
        simplest implementation may just be
        `return self.game_result() is not None`
        Returns
        -------
        boolean
        """
        return self.game_result is not None

    def move(self, action):
        self.played_cards.append(action.card)
        # print_hand(self.p1_hand)
        # print_hand(self.p2_hand)

        # print_hand(self.p2_hand)
        # print(self.next_to_move)
        # print_card(self.played_card)
        # print_card(action.card)
        if self.next_to_move == 0:
            self.p1_hand.remove(action.card)
        else:
            self.p2_hand.remove(action.card)

        if self.played_card is None:  # play first card, switch player
            self.played_card = action.card
            # print(self.played_card)
            if self.next_to_move == 0:
                self.next_to_move = 1
            else:
                self.next_to_move = 0
        else:  # respond to played card
            is_stronger = stronger_card(self.played_card, action.card)
            # print(is_stronger)
            if self.next_to_move == 1:  # p1 played first
                if is_stronger:  # p2 won hand
                    self.next_to_move = 1
                    self.points[1] += (
                        points[get_number(self.played_card)]
                        + points[get_number(action.card)]
                    )
                else:
                    self.next_to_move = 0
                    self.points[0] += (
                        points[get_number(self.played_card)]
                        + points[get_number(action.card)]
                    )
            else:  # p2 played first
                if is_stronger:  # p1 won hand
                    self.next_to_move = 0
                    self.points[0] += (
                        points[get_number(self.played_card)]
                        + points[get_number(action.card)]
                    )
                else:
                    self.next_to_move = 1
                    self.points[1] += (
                        points[get_number(self.played_card)]
                        + points[get_number(action.card)]
                    )
            if len(self.remaining_cards):  # draw new cards
                random.shuffle(self.remaining_cards)
                # print_card(self.remaining_cards[0])
                # print_card(self.remaining_cards[1])
                # print_hand(self.remaining_cards)
                self.p1_hand.append(self.remaining_cards[0])
                self.p2_hand.append(self.remaining_cards[1])
                # self.remaining_cards = self.remaining_cards[2:-2]
                # print_hand(self.remaining_cards)
            self.played_card = None

        # print(f"played: {self.played_card}, next to move {self.next_to_move}")
        return Treseta(
            points=self.points,
            p1_hand=sorted(self.p1_hand),
            p2_hand=sorted(self.p2_hand),
            played_card=self.played_card,
            played_cards=self.played_cards,
            next_to_move=self.next_to_move,
        )
        # played_card = action.card

        """
        consumes action and returns resulting TwoPlayersAbstractGameState
        Parameters
        ----------
        action: AbstractGameAction
        Returns
        -------
        TwoPlayersAbstractGameState
        """
        pass

    def get_legal_actions(self):
        """
        returns list of legal action at current game state
        Returns
        -------
        list of AbstractGameAction
        """
        if self.played_card is None:
            if self.next_to_move == 0:
                return [PlayCard(card) for card in self.p1_hand]
            else:
                return [PlayCard(card) for card in self.p2_hand]

        if self.next_to_move == 0:
            legal_cards = legal_options(self.p1_hand, self.played_card)
        else:
            legal_cards = legal_options(self.p2_hand, self.played_card)

        return [PlayCard(card) for card in legal_cards]


# class AbstractGameAction(ABC):
#    pass