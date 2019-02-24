import random

import pytest

from scythe_automa_ai import scythe_faction_creator
from scythe_automa_ai.scythe_faction_creator import VALID_FACTIONS, ScytheFaction, InvalidFactionException, \
    INITIAL_COMBAT_CARDS, INITIAL_POWER, FACTION_ABILITY, MECH_ONE_ABILITY, MECH_TWO_ABILITY, MECH_THREE_ABILITY, \
    MECH_FOUR_ABILITY


def helper_to_create_dict_for_default_values(default_power, default_combat_cards, default_faction_power,
                                             mech_one_ability, mech_two_ability, mech_three_ability, mech_four_ability):
    to_return = dict()
    to_return[INITIAL_POWER] = default_power
    to_return[INITIAL_COMBAT_CARDS] = default_combat_cards
    to_return[FACTION_ABILITY] = default_faction_power
    to_return[MECH_ONE_ABILITY] = mech_one_ability
    to_return[MECH_TWO_ABILITY] = mech_two_ability
    to_return[MECH_THREE_ABILITY] = mech_three_ability
    to_return[MECH_FOUR_ABILITY] = mech_four_ability
    return to_return


def helper_for_test_to_make_sure_default_values_are_correct(created_faction_to_test_for, dict_of_default_values):
    assert dict_of_default_values[INITIAL_POWER] == created_faction_to_test_for.initial_power
    assert dict_of_default_values[INITIAL_COMBAT_CARDS] == created_faction_to_test_for.initial_combat_cards
    assert dict_of_default_values[FACTION_ABILITY] == created_faction_to_test_for.faction_ability
    assert dict_of_default_values[MECH_ONE_ABILITY] == created_faction_to_test_for.mech_one_ability
    assert dict_of_default_values[MECH_TWO_ABILITY] == created_faction_to_test_for.mech_two_ability
    assert dict_of_default_values[MECH_THREE_ABILITY] == created_faction_to_test_for.mech_three_ability
    assert dict_of_default_values[MECH_FOUR_ABILITY] == created_faction_to_test_for.mech_four_ability


def test_faction_list_contains_albion_faction():
    albion_faction = 'albion'
    assert albion_faction in VALID_FACTIONS


def test_albion_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(3, 0, 'exalt', 'burrow', 'sword', 'shield', 'rally')
    scythe_faction = ScytheFaction(scythe_faction_creator.ALBION)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_crimea_faction():
    crimea_faction = 'crimea'
    assert crimea_faction in VALID_FACTIONS


def test_crimea_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(5, 0, 'coercion', 'riverwalk_crimea', 'wayfare', 'scout',
                                                              'speed')
    scythe_faction = ScytheFaction(scythe_faction_creator.CRIMEA)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_nordic_faction():
    nordic_faction = 'nordic'
    assert nordic_faction in VALID_FACTIONS


def test_nordic_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(4, 1, 'swim', 'riverwalk_nordic', 'seaworthy',
                                                              'artillery', 'speed')
    scythe_faction = ScytheFaction(scythe_faction_creator.NORDIC)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_polania_faction():
    polania_faction = 'polania'
    assert polania_faction in VALID_FACTIONS


def test_polania_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(2, 3, 'meander', 'riverwalk_polania', 'submerge',
                                                              'camaraderie', 'speed')
    scythe_faction = ScytheFaction(scythe_faction_creator.POLANIA)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_rusviet_faction():
    rusviet_faction = 'rusviet'
    assert rusviet_faction in VALID_FACTIONS


def test_rusviet_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(3, 2, 'relentless', 'riverwalk_rusviet', 'township',
                                                              'peoples_army', 'speed')
    scythe_faction = ScytheFaction(scythe_faction_creator.RUSVIET)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_saxony_faction():
    saxony_faction = 'saxony'
    assert saxony_faction in VALID_FACTIONS


def test_saxony_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(1, 4, 'dominate', 'riverwalk_saxony', 'underpass',
                                                              'disarm', 'speed')
    scythe_faction = ScytheFaction(scythe_faction_creator.SAXONY)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_togawa_faction():
    togawa_faction = 'togawa'
    assert togawa_faction in VALID_FACTIONS


def test_togawa_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(0, 2, 'maifuku', 'toka', 'suiton', 'ronin', 'shinobi')
    scythe_faction = ScytheFaction(scythe_faction_creator.TOGAWA)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_created_is_faction_asked_for():
    any_faction = random.choice(VALID_FACTIONS)
    faction_board = ScytheFaction(any_faction)
    assert any_faction == faction_board.faction, "Factions are not the same"


def test_faction_creation_fails_if_invalid_faction_requested():
    invalid_faction = 'this_is_not_a_real_faction'
    with pytest.raises(InvalidFactionException) as e_info:
        ScytheFaction(invalid_faction)


def test_only_seven_factions_exist():
    assert len(VALID_FACTIONS) == 7
