import random

from scythe_automa_ai.scythe_faction_creator import VALID_FACTIONS, ScytheFaction
from scythe_automa_ai.scythe_player_mat_creator import VALID_PLAYER_MATS, ScythePlayerMat


class ScytheGameStateManager():

    def __init__(self, automa_level='autometta'):
        self.automa_level = automa_level
        self.player_faction = ScytheFaction(random.choice(VALID_FACTIONS))
        factions_besides_player_faction = list(filter(lambda x: x != self.player_faction.faction_name, VALID_FACTIONS))
        self.automa_faction = ScytheFaction(random.choice(factions_besides_player_faction))
        self.player_mat = ScythePlayerMat(random.choice(VALID_PLAYER_MATS))
