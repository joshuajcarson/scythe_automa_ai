VALID_FACTIONS = ['albion', 'crimea', 'nordic', 'polania', 'rusviet', 'saxony', 'togawa']


class InvalidFactionException(ValueError):
    '''To be raised when invalid factions are requested'''


class ScytheFaction():

    def __init__(self, faction):
        if faction not in VALID_FACTIONS:
            raise InvalidFactionException('Invalid Faction Requested', faction)
        self.faction = faction
