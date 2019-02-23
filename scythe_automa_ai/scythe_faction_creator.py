ALBION = 'albion'
CRIMEA = 'crimea'
NORDIC = 'nordic'
POLANIA = 'polania'
RUSVIET = 'rusviet'
SAXONY = 'saxony'
TOGAWA = 'togawa'
VALID_FACTIONS = [ALBION, CRIMEA, NORDIC, POLANIA, RUSVIET, SAXONY, TOGAWA]


class InvalidFactionException(ValueError):
    """To be raised when invalid factions are requested"""


def base_power_for_faction(faction):
    if faction == ALBION:
        return 3
    elif faction == POLANIA:
        return 2
    return 1


def base_combat_cards_for_faction(faction):
    if faction == ALBION:
        return 0
    elif faction == POLANIA:
        return 3
    return 4


class ScytheFaction():

    def __init__(self, faction):
        if faction not in VALID_FACTIONS:
            raise InvalidFactionException('Invalid Faction Requested', faction)
        self.faction = faction
        self.base_power = base_power_for_faction(faction)
        self.base_combat_cards = base_combat_cards_for_faction(faction)
