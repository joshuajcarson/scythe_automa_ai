import random
import pytest

from scythe_automa_ai.scythe_faction_creator import VALID_FACTIONS, ScytheFaction, InvalidFactionException


def test_faction_list_contains_rusviet_faction():
    rusviet_faction = 'rusviet'
    assert rusviet_faction in VALID_FACTIONS


def test_faction_list_contains_crimea_faction():
    crimea_faction = 'crimea'
    assert crimea_faction in VALID_FACTIONS


def test_faction_list_contains_nordic_faction():
    nordic_faction = 'nordic'
    assert nordic_faction in VALID_FACTIONS


def test_faction_list_contains_togawa_faction():
    togawa_faction = 'togawa'
    assert togawa_faction in VALID_FACTIONS


def test_faction_list_contains_polania_faction():
    polania_faction = 'polania'
    assert polania_faction in VALID_FACTIONS


def test_faction_list_contains_albion_faction():
    albion_faction = 'albion'
    assert albion_faction in VALID_FACTIONS


def test_faction_list_contains_saxony_faction():
    saxony_faction = 'saxony'
    assert saxony_faction in VALID_FACTIONS


def test_faction_created_is_faction_asked_for():
    any_faction = random.choice(VALID_FACTIONS)
    faction_board = ScytheFaction(any_faction)
    assert any_faction == faction_board.faction, "Factions are not the same"


def test_faction_creation_fails_if_invalid_faction_requested():
    invalid_faction = 'this_is_not_a_real_faction'
    with pytest.raises(InvalidFactionException) as e_info:
        ScytheFaction(invalid_faction)
