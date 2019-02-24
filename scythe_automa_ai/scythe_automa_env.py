import random

from scythe_automa_ai.scythe_faction_creator import VALID_FACTIONS, ScytheFaction


class ScytheGameStateManager():

    def __init__(self, automa_level='autometta'):
        self.automa_level = automa_level
        self.player_faction = ScytheFaction(random.choice(VALID_FACTIONS))
        self.automa_faction = ScytheFaction(random.choice(list(filter(lambda x : x != self.player_faction, VALID_FACTIONS))))
