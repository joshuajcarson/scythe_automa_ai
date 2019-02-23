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
FACTION_STARTING_DATA_FRAME = pd.DataFrame(np.array([[3, 0, 'exalt'],
                                                     [5, 0, 'coercion'],
                                                     [4, 1, 'swim'],
                                                     [2, 3, 'meander'],
                                                     [3, 2, 'relentless'],
                                                     [1, 4, 'dominate'],
                                                     [0, 2, 'maifuku']]),
                                           columns=['base_power', 'base_combat_cards', 'base_faction_power'],
                                           index=[ALBION, CRIMEA, NORDIC, POLANIA, RUSVIET, SAXONY, TOGAWA])
FACTION_STARTING_DATA_FRAME.base_power = pd.to_numeric(FACTION_STARTING_DATA_FRAME.base_power)
FACTION_STARTING_DATA_FRAME.base_combat_cards = pd.to_numeric(FACTION_STARTING_DATA_FRAME.base_combat_cards)


class InvalidFactionException(ValueError):
    """To be raised when invalid factions are requested"""


def base_power_for_faction(faction):
    return FACTION_STARTING_DATA_FRAME.loc[faction, 'base_power']


def base_combat_cards_for_faction(faction):
    return FACTION_STARTING_DATA_FRAME.loc[faction, 'base_combat_cards']


def base_faction_power_for_faction(faction):
    return FACTION_STARTING_DATA_FRAME.loc[faction, 'base_faction_power']


class ScytheFaction():

    def __init__(self, faction):
        if faction not in VALID_FACTIONS:
            raise InvalidFactionException('Invalid Faction Requested', faction)
        self.faction = faction
        self.base_power = base_power_for_faction(faction)
        self.base_combat_cards = base_combat_cards_for_faction(faction)
        self.base_faction_power = base_faction_power_for_faction(faction)
