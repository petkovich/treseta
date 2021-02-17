import numpy as np
from mctspy.tree.nodes import TwoPlayersGameMonteCarloTreeSearchNode
from mctspy.tree.search import MonteCarloTreeSearch
from mctspy.games.examples.tictactoe import TicTacToeGameState
from mc_treseta import Treseta
import random
from game import *

cards = list(range(40))
p1_cards = cards[0:9] + [cards[31]]
p2_cards = cards[10:16] + cards[35:39]
print_hand(sorted(p1_cards))
print_hand(sorted(p2_cards))

initial_game_state = Treseta(
    points=[0, 0],
    p1_hand=p1_cards,
    p2_hand=p2_cards,
    played_card=None,
    played_cards=[],
    next_to_move=0,
)

root = TwoPlayersGameMonteCarloTreeSearchNode(state=initial_game_state)
mcts = MonteCarloTreeSearch(root)
best_node = mcts.best_action(100)
print_hand(best_node.state.played_cards)
print(best_node.state.played_card)
print(best_node.state.points)

# state = np.zeros((3, 3))
# state[0][0] = -1
# initial_board_state = TicTacToeGameState(state=state, next_to_move=1)
# root = TwoPlayersGameMonteCarloTreeSearchNode(state=initial_board_state)
# mcts = MonteCarloTreeSearch(root)
# best_node = mcts.best_action(100)
# print(best_node.state.board)
