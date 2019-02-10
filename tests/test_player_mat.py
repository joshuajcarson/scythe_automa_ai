from gym_scythe import player_mat
import pytest

def test_mat_contains_trade_action():
    test_player_mat = player_mat.get_player_mat()
    assert "trade" == test_player_mat['actions'];
