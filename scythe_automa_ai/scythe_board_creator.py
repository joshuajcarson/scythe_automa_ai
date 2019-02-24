import numpy as np
import pandas as pd

IDENTIFIER = 'identifier'
U_CORD = 'u'
V_CORD = 'v'

STARTING_BOARD = pd.DataFrame(np.array([[-4, 7, 'saxony_home_base']]),
                              columns=[U_CORD, V_CORD, IDENTIFIER])
STARTING_BOARD[U_CORD] = pd.to_numeric(STARTING_BOARD[U_CORD])
STARTING_BOARD[V_CORD] = pd.to_numeric(STARTING_BOARD[V_CORD])


class ScytheBoard():
    def __init__(self):
        self.tiles = STARTING_BOARD.copy()
