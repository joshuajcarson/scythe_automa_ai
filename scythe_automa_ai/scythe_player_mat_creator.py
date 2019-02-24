import numpy as np
import pandas as pd

INDUSTRIAL = 'industrial'
ENGINEERING = 'engineering'
MILITANT = 'militant'
PATRIOTIC = 'patriotic'
INNOVATIVE = 'innovative'
MECHANICAL = 'mechanical'
AGRICULTURAL = 'agricultural'
VALID_PLAYER_MATS = [INDUSTRIAL, ENGINEERING, MILITANT, PATRIOTIC, INNOVATIVE, MECHANICAL, AGRICULTURAL]

BOLSTER = 'bolster'
PRODUCE = 'produce'
MOVE = 'move'
TRADE = 'trade'
UPGRADE = 'upgrade'
DEPLOY = 'deploy'
BUILD = 'build'
ENLIST = 'enlist'

FAR_LEFT_TOP_ROW = 'far_left_top_row'
MIDDLE_LEFT_TOP_ROW = 'middle_left_top_row'
MIDDLE_RIGHT_TOP_ROW = 'middle_right_top_row'
FAR_RIGHT_TOP_ROW = 'far_right_top_row'

UPGRADE_INITIAL_COST = 'upgrade_initial_cost'
UPGRADE_UPGRADE_ALLOWED = 'upgrade_upgrade_allowed'
UPGRADE_GOLD_EARNED = 'upgrade_gold_earned'
DEPLOY_INITIAL_COST = 'deploy_initial_cost'
DEPLOY_UPGRADE_ALLOWED = 'deploy_upgrade_allowed'
DEPLOY_GOLD_EARNED = 'deploy_gold_earned'
BUILD_INITIAL_COST = 'build_initial_cost'
BUILD_UPGRADE_ALLOWED = 'build_upgrade_allowed'
BUILD_GOLD_EARNED = 'build_gold_earned'
ENLIST_INITIAL_COST = 'enlist_initial_cost'
ENLIST_UPGRADE_ALLOWED = 'enlist_upgrade_allowed'
ENLIST_GOLD_EARNED = 'enlist_gold_earned'

INDUSTRIAL_DATA = [BOLSTER, PRODUCE, MOVE, TRADE, 3, 1, 3, 3, 2, 2, 3, 1, 1, 4, 2, 0]
ENGINEERING_DATA = [PRODUCE, TRADE, BOLSTER, MOVE, 3, 1, 2, 4, 2, 0, 3, 2, 3, 3, 1, 1]
MILITANT_DATA = [BOLSTER, MOVE, PRODUCE, TRADE, 3, 2, 0, 3, 1, 3, 4, 1, 1, 3, 2, 2]
PATRIOTIC_DATA = [MOVE, BOLSTER, TRADE, PRODUCE, 2, 0, 1, 4, 3, 3, 4, 2, 0, 3, 1, 2]
INNOVATIVE_DATA = [TRADE, PRODUCE, BOLSTER, MOVE, 3, 0, 3, 3, 1, 1, 4, 3, 2, 4, 2, 0]
MECHANICAL_DATA = [TRADE, BOLSTER, MOVE, PRODUCE, 3, 1, 0, 3, 2, 2, 3, 1, 2, 4, 2, 2]
AGRICULTURAL_DATA = [MOVE, TRADE, PRODUCE, BOLSTER, 2, 0, 1, 4, 2, 0, 4, 2, 2, 3, 2, 3]

PLAYER_MAT_DATA_FRAME = pd.DataFrame(
    np.array([INDUSTRIAL_DATA, ENGINEERING_DATA, MILITANT_DATA, PATRIOTIC_DATA, INNOVATIVE_DATA, MECHANICAL_DATA,
              AGRICULTURAL_DATA]),
    columns=[FAR_LEFT_TOP_ROW, MIDDLE_LEFT_TOP_ROW, MIDDLE_RIGHT_TOP_ROW, FAR_RIGHT_TOP_ROW, UPGRADE_INITIAL_COST,
             UPGRADE_UPGRADE_ALLOWED, UPGRADE_GOLD_EARNED, DEPLOY_INITIAL_COST, DEPLOY_UPGRADE_ALLOWED,
             DEPLOY_GOLD_EARNED, BUILD_INITIAL_COST, BUILD_UPGRADE_ALLOWED, BUILD_GOLD_EARNED, ENLIST_INITIAL_COST,
             ENLIST_UPGRADE_ALLOWED, ENLIST_GOLD_EARNED],
    index=[INDUSTRIAL, ENGINEERING, MILITANT, PATRIOTIC, INNOVATIVE, MECHANICAL, AGRICULTURAL])
PLAYER_MAT_DATA_FRAME[UPGRADE_INITIAL_COST] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[UPGRADE_INITIAL_COST])
PLAYER_MAT_DATA_FRAME[UPGRADE_UPGRADE_ALLOWED] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[UPGRADE_UPGRADE_ALLOWED])
PLAYER_MAT_DATA_FRAME[UPGRADE_GOLD_EARNED] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[UPGRADE_GOLD_EARNED])
PLAYER_MAT_DATA_FRAME[DEPLOY_INITIAL_COST] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[DEPLOY_INITIAL_COST])
PLAYER_MAT_DATA_FRAME[DEPLOY_UPGRADE_ALLOWED] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[DEPLOY_UPGRADE_ALLOWED])
PLAYER_MAT_DATA_FRAME[DEPLOY_GOLD_EARNED] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[DEPLOY_GOLD_EARNED])
PLAYER_MAT_DATA_FRAME[BUILD_INITIAL_COST] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[BUILD_INITIAL_COST])
PLAYER_MAT_DATA_FRAME[BUILD_UPGRADE_ALLOWED] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[BUILD_UPGRADE_ALLOWED])
PLAYER_MAT_DATA_FRAME[BUILD_GOLD_EARNED] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[BUILD_GOLD_EARNED])
PLAYER_MAT_DATA_FRAME[ENLIST_INITIAL_COST] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[ENLIST_INITIAL_COST])
PLAYER_MAT_DATA_FRAME[ENLIST_UPGRADE_ALLOWED] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[ENLIST_UPGRADE_ALLOWED])
PLAYER_MAT_DATA_FRAME[ENLIST_GOLD_EARNED] = pd.to_numeric(PLAYER_MAT_DATA_FRAME[ENLIST_GOLD_EARNED])


class InvalidPlayerMatException(ValueError):
    """To be raised when invalid factions are requested"""


def far_left_top_row_for_player(player):
    return PLAYER_MAT_DATA_FRAME.loc[player, FAR_LEFT_TOP_ROW]


def middle_left_top_row_for_player(player):
    return PLAYER_MAT_DATA_FRAME.loc[player, MIDDLE_LEFT_TOP_ROW]


def middle_right_top_row_for_player(player):
    return PLAYER_MAT_DATA_FRAME.loc[player, MIDDLE_RIGHT_TOP_ROW]


def far_right_top_row_for_player(player):
    return PLAYER_MAT_DATA_FRAME.loc[player, FAR_RIGHT_TOP_ROW]


class ScythePlayerMat():
    def __init__(self, player_mat_name):
        if player_mat_name not in VALID_PLAYER_MATS:
            raise InvalidPlayerMatException('Invalid Player Mat Requested', player_mat_name)
        self.name = player_mat_name
        self.far_left_top_row = far_left_top_row_for_player(player_mat_name)
        self.middle_left_top_row = middle_left_top_row_for_player(player_mat_name)
        self.middle_right_top_row = middle_right_top_row_for_player(player_mat_name)
        self.far_right_top_row = far_right_top_row_for_player(player_mat_name)
