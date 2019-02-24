import numpy as np
import pandas as pd

INITIAL_POWER = 'initial_power'
INITIAL_COMBAT_CARDS = 'initial_combat_cards'
FACTION_ABILITY = 'faction_ability'
MECH_ONE_ABILITY = 'mech_one_ability'
MECH_TWO_ABILITY = 'mech_two_ability'
MECH_THREE_ABILITY = 'mech_three_ability'
MECH_FOUR_ABILITY = 'mech_four_ability'

ALBION = 'albion'
CRIMEA = 'crimea'
NORDIC = 'nordic'
POLANIA = 'polania'
RUSVIET = 'rusviet'
SAXONY = 'saxony'
TOGAWA = 'togawa'
VALID_FACTIONS = [ALBION, CRIMEA, NORDIC, POLANIA, RUSVIET, SAXONY, TOGAWA]

ALBION_DATA = [3, 0, 'exalt', 'burrow', 'sword', 'shield', 'rally']
CRIMEA_DATA = [5, 0, 'coercion', 'riverwalk_crimea', 'wayfare', 'scout', 'speed']
NORDIC_DATA = [4, 1, 'swim', 'riverwalk_nordic', 'seaworthy', 'artillery', 'speed']
POLANIA_DATA = [2, 3, 'meander', 'riverwalk_polania', 'submerge', 'camaraderie', 'speed']
RUSVIET_DATA = [3, 2, 'relentless', 'riverwalk_rusviet', 'township', 'peoples_army', 'speed']
SAXONY_DATA = [1, 4, 'dominate', 'riverwalk_saxony', 'underpass', 'disarm', 'speed']
TOGAWA_DATA = [0, 2, 'maifuku', 'toka', 'suiton', 'ronin', 'shinobi']

FACTION_STARTING_DATA_FRAME = pd.DataFrame(
    np.array([ALBION_DATA, CRIMEA_DATA, NORDIC_DATA, POLANIA_DATA, RUSVIET_DATA, SAXONY_DATA, TOGAWA_DATA]),
    columns=[INITIAL_POWER, INITIAL_COMBAT_CARDS, FACTION_ABILITY, MECH_ONE_ABILITY, MECH_TWO_ABILITY,
             MECH_THREE_ABILITY, MECH_FOUR_ABILITY],
    index=[ALBION, CRIMEA, NORDIC, POLANIA, RUSVIET, SAXONY, TOGAWA])
FACTION_STARTING_DATA_FRAME[INITIAL_POWER] = pd.to_numeric(FACTION_STARTING_DATA_FRAME[INITIAL_POWER])
FACTION_STARTING_DATA_FRAME[INITIAL_COMBAT_CARDS] = pd.to_numeric(FACTION_STARTING_DATA_FRAME[INITIAL_COMBAT_CARDS])


class InvalidFactionException(ValueError):
    """To be raised when invalid factions are requested"""


class ScytheFaction():

    def __init__(self, faction_name):
        if faction_name not in VALID_FACTIONS:
            raise InvalidFactionException('Invalid Faction Requested', faction_name)
        self.faction = faction_name
        self.player_data = FACTION_STARTING_DATA_FRAME.loc[faction_name]
