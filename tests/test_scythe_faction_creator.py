import random

import pytest

from scythe_automa_ai import scythe_faction_creator
from scythe_automa_ai.scythe_faction_creator import VALID_FACTIONS, ScytheFaction, InvalidFactionException


def test_faction_list_contains_albion_faction():
    albion_faction = 'albion'
    assert albion_faction in VALID_FACTIONS


def test_albion_faction_defaults_to_correct_base():
    base_power = 3
    base_combat_cards = 0
    base_faction_power = 'exalt'
    scythe_faction = ScytheFaction(scythe_faction_creator.ALBION)
    assert base_power == scythe_faction.base_power
    assert base_combat_cards == scythe_faction.base_combat_cards
    assert base_faction_power == scythe_faction.base_faction_power


def test_faction_list_contains_crimea_faction():
    crimea_faction = 'crimea'
    assert crimea_faction in VALID_FACTIONS


def test_crimea_faction_defaults_to_correct_base():
    base_power = 5
    base_combat_cards = 0
    base_faction_power = 'coercion'
    scythe_faction = ScytheFaction(scythe_faction_creator.CRIMEA)
    assert base_power == scythe_faction.base_power
    assert base_combat_cards == scythe_faction.base_combat_cards
    assert base_faction_power == scythe_faction.base_faction_power


def test_faction_list_contains_nordic_faction():
    nordic_faction = 'nordic'
    assert nordic_faction in VALID_FACTIONS


def test_nordic_faction_defaults_to_correct_base():
    base_power = 4
    base_combat_cards = 1
    base_faction_power = 'swim'
    scythe_faction = ScytheFaction(scythe_faction_creator.NORDIC)
    assert base_power == scythe_faction.base_power
    assert base_combat_cards == scythe_faction.base_combat_cards
    assert base_faction_power == scythe_faction.base_faction_power


def test_faction_list_contains_polania_faction():
    polania_faction = 'polania'
    assert polania_faction in VALID_FACTIONS


def test_polania_faction_defaults_to_correct_base():
    base_power = 2
    base_combat_cards = 3
    base_faction_power = 'meander'
    scythe_faction = ScytheFaction(scythe_faction_creator.POLANIA)
    assert base_power == scythe_faction.base_power
    assert base_combat_cards == scythe_faction.base_combat_cards
    assert base_faction_power == scythe_faction.base_faction_power


def test_faction_list_contains_rusviet_faction():
    rusviet_faction = 'rusviet'
    assert rusviet_faction in VALID_FACTIONS


def test_rusviet_faction_defaults_to_correct_base():
    base_power = 3
    base_combat_cards = 2
    base_faction_power = 'relentless'
    scythe_faction = ScytheFaction(scythe_faction_creator.RUSVIET)
    assert base_power == scythe_faction.base_power
    assert base_combat_cards == scythe_faction.base_combat_cards
    assert base_faction_power == scythe_faction.base_faction_power


def test_faction_list_contains_saxony_faction():
    saxony_faction = 'saxony'
    assert saxony_faction in VALID_FACTIONS


def test_saxony_faction_defaults_to_correct_base():
    base_power = 1
    base_combat_cards = 4
    base_faction_power = 'dominate'
    scythe_faction = ScytheFaction(scythe_faction_creator.SAXONY)
    assert base_power == scythe_faction.base_power
    assert base_combat_cards == scythe_faction.base_combat_cards
    assert base_faction_power == scythe_faction.base_faction_power


def test_faction_list_contains_togawa_faction():
    togawa_faction = 'togawa'
    assert togawa_faction in VALID_FACTIONS


def test_togawa_faction_defaults_to_correct_base():
    base_power = 0
    base_combat_cards = 2
    base_faction_power = 'maifuku'
    scythe_faction = ScytheFaction(scythe_faction_creator.TOGAWA)
    assert base_power == scythe_faction.base_power
    assert base_combat_cards == scythe_faction.base_combat_cards
    assert base_faction_power == scythe_faction.base_faction_power


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
