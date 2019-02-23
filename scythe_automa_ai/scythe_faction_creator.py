import numpy as np
import pandas as pd

ALBION = 'albion'
CRIMEA = 'crimea'
NORDIC = 'nordic'
POLANIA = 'polania'
RUSVIET = 'rusviet'
SAXONY = 'saxony'
TOGAWA = 'togawa'
VALID_FACTIONS = [ALBION, CRIMEA, NORDIC, POLANIA, RUSVIET, SAXONY, TOGAWA]
FACTION_STARTING_DATA_FRAME = pd.DataFrame(np.array([[3, 0], [5, 0], [4, 1], [2, 3], [3, 2], [1, 4], [0, 2]]),
                                           columns=['base_power', 'base_combat_cards'],
                                           index=[ALBION, CRIMEA, NORDIC, POLANIA, RUSVIET, SAXONY, TOGAWA])


class InvalidFactionException(ValueError):
    """To be raised when invalid factions are requested"""


def base_power_for_faction(faction):
    return FACTION_STARTING_DATA_FRAME.loc[faction, 'base_power']


def base_combat_cards_for_faction(faction):
    return FACTION_STARTING_DATA_FRAME.loc[faction, 'base_combat_cards']


class ScytheFaction():

    def __init__(self, faction):
        if faction not in VALID_FACTIONS:
            raise InvalidFactionException('Invalid Faction Requested', faction)
        self.faction = faction
        self.base_power = base_power_for_faction(faction)
        self.base_combat_cards = base_combat_cards_for_faction(faction)
