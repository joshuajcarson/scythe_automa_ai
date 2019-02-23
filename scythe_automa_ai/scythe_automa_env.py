import random

VALID_FACTIONS = ['albion', 'crimea', 'nordic', 'polania', 'rusviet', 'saxony', 'togawa']


class ScytheGameStateManager():

    def __init__(self, automa_level='autometta'):
        self.automa_level = automa_level
        self.player_faction = random.choice(VALID_FACTIONS)
        self.automa_faction = random.choice(list(filter(lambda x : x != self.player_faction, VALID_FACTIONS)))
