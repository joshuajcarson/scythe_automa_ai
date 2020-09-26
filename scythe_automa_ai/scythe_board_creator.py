import numpy as np
import pandas as pd
from scythe_automa_ai.scythe_faction_creator import SAXONY, ALBION

TYPE = 'type'
IDENTIFIER = 'identifier'
TUNNEL = 'tunnel'
HOME_BASE = 'home_base'
TOP_LEFT_RIVER = 'top_left_river'
TOP_RIGHT_RIVER = 'top_right_river'
LEFT_RIVER = 'left_river'
RIGHT_RIVER = 'right_river'
BOTTOM_LEFT_RIVER = 'bottom_left_river'
BOTTOM_RIGHT_RIVER = 'bottom_right_river'
MOUNTAIN = 'mountain'
U_CORD = 'u'
V_CORD = 'v'

STARTING_BOARD = pd.DataFrame(np.array([[-4, 7, HOME_BASE, SAXONY, "", "", "", "", "", "", ""],
                                        [1, 0, HOME_BASE, ALBION, "", "", "", "", "", "", ""],
                                        [0, 3, MOUNTAIN, "", 'True', "", "", "True", "", "True", ""]]),
                              columns=[U_CORD, V_CORD, TYPE, IDENTIFIER, TUNNEL, TOP_LEFT_RIVER, TOP_RIGHT_RIVER,
                                       LEFT_RIVER, RIGHT_RIVER, BOTTOM_LEFT_RIVER, BOTTOM_RIGHT_RIVER])
STARTING_BOARD[U_CORD] = pd.to_numeric(STARTING_BOARD[U_CORD])
STARTING_BOARD[V_CORD] = pd.to_numeric(STARTING_BOARD[V_CORD])
STARTING_BOARD[TUNNEL] = STARTING_BOARD[TUNNEL].astype('bool')
STARTING_BOARD[TOP_LEFT_RIVER] = STARTING_BOARD[TOP_LEFT_RIVER].astype('bool')
STARTING_BOARD[TOP_RIGHT_RIVER] = STARTING_BOARD[TOP_RIGHT_RIVER].astype('bool')
STARTING_BOARD[LEFT_RIVER] = STARTING_BOARD[LEFT_RIVER].astype('bool')
STARTING_BOARD[RIGHT_RIVER] = STARTING_BOARD[RIGHT_RIVER].astype('bool')
STARTING_BOARD[BOTTOM_LEFT_RIVER] = STARTING_BOARD[BOTTOM_LEFT_RIVER].astype('bool')
STARTING_BOARD[BOTTOM_RIGHT_RIVER] = STARTING_BOARD[BOTTOM_RIGHT_RIVER].astype('bool')
STARTING_BOARD = STARTING_BOARD.set_index([U_CORD, V_CORD])


class ScytheBoard():
    def __init__(self):
        self.tiles = STARTING_BOARD.copy()
