import random

import pytest

from scythe_automa_ai import scythe_faction_creator
from scythe_automa_ai.scythe_faction_creator import VALID_FACTIONS, ScytheFaction, InvalidFactionException, \
    BASE_COMBAT_CARDS, BASE_POWER, BASE_FACTION_POWER


def helper_to_create_dict_for_default_values(default_power, default_combat_cards, default_faction_power):
    to_return = dict()
    to_return[BASE_POWER] = default_power
    to_return[BASE_COMBAT_CARDS] = default_combat_cards
    to_return[BASE_FACTION_POWER] = default_faction_power
    return to_return


def helper_for_test_to_make_sure_default_values_are_correct(created_faction_to_test_for, dict_of_default_values):
    assert dict_of_default_values[BASE_POWER] == created_faction_to_test_for.base_power
    assert dict_of_default_values[BASE_COMBAT_CARDS] == created_faction_to_test_for.base_combat_cards
    assert dict_of_default_values[BASE_FACTION_POWER] == created_faction_to_test_for.base_faction_power


def test_faction_list_contains_albion_faction():
    albion_faction = 'albion'
    assert albion_faction in VALID_FACTIONS


def test_albion_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(3, 0, 'exalt')
    scythe_faction = ScytheFaction(scythe_faction_creator.ALBION)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_crimea_faction():
    crimea_faction = 'crimea'
    assert crimea_faction in VALID_FACTIONS


def test_crimea_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(5, 0, 'coercion')
    scythe_faction = ScytheFaction(scythe_faction_creator.CRIMEA)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_nordic_faction():
    nordic_faction = 'nordic'
    assert nordic_faction in VALID_FACTIONS


def test_nordic_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(4, 1, 'swim')
    scythe_faction = ScytheFaction(scythe_faction_creator.NORDIC)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_polania_faction():
    polania_faction = 'polania'
    assert polania_faction in VALID_FACTIONS


def test_polania_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(2, 3, 'meander')
    scythe_faction = ScytheFaction(scythe_faction_creator.POLANIA)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_rusviet_faction():
    rusviet_faction = 'rusviet'
    assert rusviet_faction in VALID_FACTIONS


def test_rusviet_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(3, 2, 'relentless')
    scythe_faction = ScytheFaction(scythe_faction_creator.RUSVIET)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_saxony_faction():
    saxony_faction = 'saxony'
    assert saxony_faction in VALID_FACTIONS


def test_saxony_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(1, 4, 'dominate')
    scythe_faction = ScytheFaction(scythe_faction_creator.SAXONY)
    helper_for_test_to_make_sure_default_values_are_correct(scythe_faction, default_values)


def test_faction_list_contains_togawa_faction():
    togawa_faction = 'togawa'
    assert togawa_faction in VALID_FACTIONS


def test_togawa_faction_defaults_to_correct_base():
    default_values = helper_to_create_dict_for_default_values(0, 2, 'maifuku')
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
