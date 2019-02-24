import pytest

from scythe_automa_ai.scythe_player_mat_creator import ScythePlayerMat, INDUSTRIAL, BOLSTER, PRODUCE, MOVE, TRADE, \
    InvalidPlayerMatException, VALID_PLAYER_MATS


def test_player_mat_creator_fails_if_invalid_player_type_requested():
    invalid_player_mat = 'not_a_real_player_mat'
    with pytest.raises(InvalidPlayerMatException) as e_info:
        ScythePlayerMat(invalid_player_mat)


def test_valid_player_mats_has_only_seven_allowed():
    assert 7 == len(VALID_PLAYER_MATS)
    assert 'industrial' in VALID_PLAYER_MATS
    assert 'engineering' in VALID_PLAYER_MATS
    assert 'militant' in VALID_PLAYER_MATS
    assert 'patriotic' in VALID_PLAYER_MATS
    assert 'innovative' in VALID_PLAYER_MATS
    assert 'mechanical' in VALID_PLAYER_MATS
    assert 'agricultural' in VALID_PLAYER_MATS


def test_player_mat_creator_builds_industrial_as_instructed():
    player_mat = ScythePlayerMat(INDUSTRIAL)
    assert INDUSTRIAL == player_mat.name
    assert BOLSTER == player_mat.far_left_top_row
    assert PRODUCE == player_mat.middle_left_top_row
    assert MOVE == player_mat.middle_right_top_row
    assert TRADE == player_mat.far_right_top_row
