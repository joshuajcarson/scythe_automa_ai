import random
import unittest.mock

import pytest

from scythe_automa_ai.scythe_automa_env import ScytheGameStateManager
from scythe_automa_ai.scythe_faction_creator import VALID_FACTIONS
from scythe_automa_ai.scythe_player_mat_creator import VALID_PLAYER_MATS


@pytest.fixture(scope='module')
def default_game_board():
    default_game_board = ScytheGameStateManager()
    return default_game_board


def test_newly_created_environment_defaults_to_automa_level_of_autometta(default_game_board):
    autometta_level = 'autometta'
    assert autometta_level == default_game_board.automa_level, 'Automa level not defaulted to autometta'


def test_newly_created_environment_has_automa_level_set_to_value_specified():
    any_automa_level = 'ultimaszyna'
    game_board = ScytheGameStateManager(automa_level=any_automa_level)
    assert any_automa_level == game_board.automa_level, 'Automa level not set based on inputed value'


def test_newly_created_environment_has_player_set_to_valid_faction(default_game_board):
    if default_game_board.player_faction.faction_name not in VALID_FACTIONS:
        assert False, "Default player faction not one of the seven valid factions and instead was {}".format(
            default_game_board.player_faction.faction_name)


def test_newly_created_environment_uses_random_choice_to_determine_faction_for_player(mocker):
    with unittest.mock.patch.object(random, 'choice', wraps=random.choice) as spy:
        ScytheGameStateManager()
        spy.assert_any_call(VALID_PLAYER_MATS)


def test_newly_created_environment_uses_unique_faction_from_player_to_determine_faction_for_automa():
    randomized_game_board = ScytheGameStateManager()
    assert randomized_game_board.player_faction.faction_name != randomized_game_board.automa_faction.faction_name, \
        "Player faction and Automa faction were the same"
    assert randomized_game_board.automa_faction.faction_name in VALID_FACTIONS


def test_newly_created_environment_has_player_set_to_valid_player_mat(default_game_board):
    if default_game_board.player_mat.player_mat_name not in VALID_PLAYER_MATS:
        assert False, "Default player mat not one of the seven valid mats and instead was {}".format(
            default_game_board.player_faction)


def test_newly_created_environment_uses_random_choice_to_determine_player_mat_for_player(mocker):
    with unittest.mock.patch.object(random, 'choice', wraps=random.choice) as spy:
        ScytheGameStateManager()
        spy.assert_any_call(VALID_FACTIONS)
