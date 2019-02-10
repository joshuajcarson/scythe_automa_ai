import pytest

from scythe_automa_ai.scythe_automa_env import ScytheGameStateManager


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
    valid_factions = {'albion', 'crimea', 'nordic', 'polania', 'rusviet', 'saxony', 'togawa'}
    if default_game_board.player_faction not in valid_factions:
        assert False, "Default player faction not one of the seven valid factions and instead was {}".format(default_game_board.player_faction)
