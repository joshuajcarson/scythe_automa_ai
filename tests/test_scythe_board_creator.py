import pytest

from scythe_automa_ai.scythe_board_creator import ScytheBoard, TYPE, TUNNEL, TOP_LEFT_RIVER, TOP_RIGHT_RIVER, \
    LEFT_RIVER, RIGHT_RIVER, BOTTOM_LEFT_RIVER, BOTTOM_RIGHT_RIVER, HOME_BASE, IDENTIFIER, MOUNTAIN
from scythe_automa_ai.scythe_faction_creator import SAXONY


@pytest.fixture(scope='module')
def default_game_tiles():
    default_game_tiles = ScytheBoard().tiles
    return default_game_tiles


def test_board_has_home_base_for_saxony(default_game_tiles):
    tile_under_test = default_game_tiles.loc[-4, 7]
    assert HOME_BASE == tile_under_test.loc[TYPE]
    assert SAXONY == tile_under_test.loc[IDENTIFIER]
    assert not tile_under_test.loc[TUNNEL]
    assert not tile_under_test.loc[TOP_LEFT_RIVER]
    assert not tile_under_test.loc[TOP_RIGHT_RIVER]
    assert not tile_under_test.loc[LEFT_RIVER]
    assert not tile_under_test.loc[RIGHT_RIVER]
    assert not tile_under_test.loc[BOTTOM_LEFT_RIVER]
    assert not tile_under_test.loc[BOTTOM_RIGHT_RIVER]


def test_top_left_tunnel_is_properly_setup(default_game_tiles):
    tile_under_test = default_game_tiles.loc[0, 3]
    assert MOUNTAIN == tile_under_test.loc[TYPE]
    assert "" == tile_under_test.loc[IDENTIFIER]
    assert tile_under_test.loc[TUNNEL]
    assert not tile_under_test.loc[TOP_LEFT_RIVER]
    assert not tile_under_test.loc[TOP_RIGHT_RIVER]
    assert tile_under_test.loc[LEFT_RIVER]
    assert not tile_under_test.loc[RIGHT_RIVER]
    assert tile_under_test.loc[BOTTOM_LEFT_RIVER]
    assert not tile_under_test.loc[BOTTOM_RIGHT_RIVER]
