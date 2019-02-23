import random

from scythe_automa_ai.scythe_faction_creator import VALID_FACTIONS


class ScytheGameStateManager():

    def __init__(self, automa_level='autometta'):
        self.automa_level = automa_level
        self.player_faction = random.choice(VALID_FACTIONS)
        self.automa_faction = random.choice(list(filter(lambda x : x != self.player_faction, VALID_FACTIONS)))
