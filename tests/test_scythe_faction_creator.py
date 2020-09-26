import random

import pytest

from scythe_automa_ai.scythe_faction_creator import VALID_FACTIONS, ScytheFaction, InvalidFactionException, \
    FACTION_STARTING_DATA_FRAME, ALBION, CRIMEA, NORDIC, POLANIA, RUSVIET, SAXONY, TOGAWA


def help_make_sure_values_exist_as_they_should(faction_name, faction_values):
    scythe_faction = ScytheFaction(faction_name)
    for i in range(0, len(faction_values)):
        faction_values[i] == scythe_faction.player_data[i]


def test_faction_data_frame_has_columns_in_correct_order():
    columns_that_should_be_in_faction_frame = ['initial_power', 'initial_combat_cards', 'faction_ability',
                                               'mech_one_ability', 'mech_two_ability', 'mech_three_ability',
                                               'mech_four_ability']
    columns_in_faction_frame = FACTION_STARTING_DATA_FRAME.columns
    for i in range(0, len(columns_that_should_be_in_faction_frame)):
        columns_that_should_be_in_faction_frame[i] == columns_in_faction_frame[i]


def test_albion_faction_defaults_to_correct_base():
    default_values = [3, 0, 'exalt', 'burrow', 'sword', 'shield', 'rally']
    help_make_sure_values_exist_as_they_should(ALBION, default_values)


def test_crimea_faction_defaults_to_correct_base():
    default_values = [5, 0, 'coercion', 'riverwalk_crimea', 'wayfare', 'scout', 'speed']
    help_make_sure_values_exist_as_they_should(CRIMEA, default_values)


def test_nordic_faction_defaults_to_correct_base():
    default_values = [4, 1, 'swim', 'riverwalk_nordic', 'seaworthy', 'artillery', 'speed']
    help_make_sure_values_exist_as_they_should(NORDIC, default_values)


def test_polania_faction_defaults_to_correct_base():
    default_values = [2, 3, 'meander', 'riverwalk_polania', 'submerge', 'camaraderie', 'speed']
    help_make_sure_values_exist_as_they_should(POLANIA, default_values)


def test_rusviet_faction_defaults_to_correct_base():
    default_values = [3, 2, 'relentless', 'riverwalk_rusviet', 'township', 'peoples_army', 'speed']
    help_make_sure_values_exist_as_they_should(RUSVIET, default_values)


def test_saxony_faction_defaults_to_correct_base():
    default_values = [1, 4, 'dominate', 'riverwalk_saxony', 'underpass', 'disarm', 'speed']
    help_make_sure_values_exist_as_they_should(SAXONY, default_values)


def test_togawa_faction_defaults_to_correct_base():
    default_values = [0, 2, 'maifuku', 'toka', 'suiton', 'ronin', 'shinobi']
    help_make_sure_values_exist_as_they_should(TOGAWA, default_values)


def test_faction_name_created_is_faction_asked_for():
    any_faction = random.choice(VALID_FACTIONS)
    faction_board = ScytheFaction(any_faction)
    assert any_faction == faction_board.faction_name, "Factions are not the same"


def test_faction_creation_fails_if_invalid_faction_requested():
    invalid_faction = 'this_is_not_a_real_faction'
    with pytest.raises(InvalidFactionException):
        ScytheFaction(invalid_faction)


def test_only_seven_factions_exist():
    assert len(VALID_FACTIONS) == 7
    assert 'albion' in VALID_FACTIONS
    assert 'crimea' in VALID_FACTIONS
    assert 'nordic' in VALID_FACTIONS
    assert 'polania' in VALID_FACTIONS
    assert 'rusviet' in VALID_FACTIONS
    assert 'saxony' in VALID_FACTIONS
    assert 'togawa' in VALID_FACTIONS
