import random

import pytest

from scythe_automa_ai import scythe_faction_creator
from scythe_automa_ai.scythe_faction_creator import VALID_FACTIONS, ScytheFaction, InvalidFactionException


def test_faction_list_contains_albion_faction():
    albion_faction = 'albion'
    assert albion_faction in VALID_FACTIONS


def test_albion_faction_defaults_to_three_power():
    albion_base_power = 3
    assert albion_base_power == ScytheFaction(scythe_faction_creator.ALBION).base_power


def test_albion_faction_defaults_to_zero_combat_cards():
    albion_base_combat_cards = 0
    assert albion_base_combat_cards == ScytheFaction(scythe_faction_creator.ALBION).base_combat_cards


def test_faction_list_contains_crimea_faction():
    crimea_faction = 'crimea'
    assert crimea_faction in VALID_FACTIONS


def test_crimea_faction_defaults_to_three_power():
    crimea_base_power = 5
    assert crimea_base_power == ScytheFaction(scythe_faction_creator.CRIMEA).base_power


def test_crimea_faction_defaults_to_zero_combat_cards():
    crimea_base_combat_cards = 0
    assert crimea_base_combat_cards == ScytheFaction(scythe_faction_creator.CRIMEA).base_combat_cards


def test_faction_list_contains_nordic_faction():
    nordic_faction = 'nordic'
    assert nordic_faction in VALID_FACTIONS


def test_nordic_faction_defaults_to_four_power():
    nordic_base_power = 4
    assert nordic_base_power == ScytheFaction(scythe_faction_creator.NORDIC).base_power


def test_nordic_faction_defaults_to_one_combat_cards():
    nordic_base_combat_cards = 1
    assert nordic_base_combat_cards == ScytheFaction(scythe_faction_creator.NORDIC).base_combat_cards


def test_faction_list_contains_polania_faction():
    polania_faction = 'polania'
    assert polania_faction in VALID_FACTIONS


def test_polania_faction_defaults_to_two_power():
    polania_base_power = 2
    assert polania_base_power == ScytheFaction(scythe_faction_creator.POLANIA).base_power


def test_polania_faction_defaults_to_three_combat_cards():
    polania_base_combat_cards = 3
    assert polania_base_combat_cards == ScytheFaction(scythe_faction_creator.POLANIA).base_combat_cards


def test_faction_list_contains_rusviet_faction():
    rusviet_faction = 'rusviet'
    assert rusviet_faction in VALID_FACTIONS


def test_rusviet_faction_defaults_to_two_power():
    rusviet_base_power = 3
    assert rusviet_base_power == ScytheFaction(scythe_faction_creator.RUSVIET).base_power


def test_rusviet_faction_defaults_to_three_combat_cards():
    rusviet_base_combat_cards = 2
    assert rusviet_base_combat_cards == ScytheFaction(scythe_faction_creator.RUSVIET).base_combat_cards


def test_faction_list_contains_saxony_faction():
    saxony_faction = 'saxony'
    assert saxony_faction in VALID_FACTIONS


def test_saxony_faction_defaults_to_one_power():
    saxony_base_power = 1
    assert saxony_base_power == ScytheFaction(scythe_faction_creator.SAXONY).base_power


def test_saxony_faction_defaults_to_four_combat_cards():
    saxony_base_combat_cards = 4
    assert saxony_base_combat_cards == ScytheFaction(scythe_faction_creator.SAXONY).base_combat_cards


def test_faction_list_contains_togawa_faction():
    togawa_faction = 'togawa'
    assert togawa_faction in VALID_FACTIONS


def test_togawa_faction_defaults_to_one_power():
    togawa_base_power = 0
    assert togawa_base_power == ScytheFaction(scythe_faction_creator.TOGAWA).base_power


def test_togawa_faction_defaults_to_four_combat_cards():
    togawa_base_combat_cards = 2
    assert togawa_base_combat_cards == ScytheFaction(scythe_faction_creator.TOGAWA).base_combat_cards


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
