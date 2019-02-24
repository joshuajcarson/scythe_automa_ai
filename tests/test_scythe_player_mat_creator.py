import pytest

from scythe_automa_ai.scythe_player_mat_creator import ScythePlayerMat, INDUSTRIAL, ENGINEERING, MILITANT, PATRIOTIC, \
    INNOVATIVE, MECHANICAL, AGRICULTURAL, BOLSTER, PRODUCE, MOVE, TRADE, \
    InvalidPlayerMatException, VALID_PLAYER_MATS, PLAYER_MAT_DATA_FRAME


def confirm_values_are_as_expected(player_mat_name, player_mat_values):
    player_mat = ScythePlayerMat(player_mat_name)
    assert player_mat_name == player_mat.name
    values_from_player_mat = player_mat.player_mat_data
    for i in range(0, len(player_mat_values)):
        assert player_mat_values[i] == values_from_player_mat[i]


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


def test_order_of_player_mat_data_columns_is_as_expected():
    columns_for_player_mat_data = ['far_left_top_row', 'middle_left_top_row', 'middle_right_top_row',
                                   'far_right_top_row', 'upgrade_initial_cost', 'upgrade_upgrade_allowed',
                                   'upgrade_gold_earned', 'deploy_initial_cost', 'deploy_upgrade_allowed',
                                   'deploy_gold_earned', 'build_initial_cost', 'build_upgrade_allowed',
                                   'build_gold_earned', 'enlist_initial_cost', 'enlist_upgrade_allowed',
                                   'enlist_gold_earned', 'starting_priority', 'initial_objectives',
                                   'initial_popularity', 'initial_coin']
    columns_in_actual_player_mat_data_frame = PLAYER_MAT_DATA_FRAME.columns
    for i in range(0, len(columns_for_player_mat_data)):
        assert columns_for_player_mat_data[i] == columns_in_actual_player_mat_data_frame[i]


def test_player_mat_creator_builds_industrial_as_instructed():
    required_values = [BOLSTER, PRODUCE, MOVE, TRADE, 3, 1, 3, 3, 2, 2, 3, 1, 1, 4, 2, 0, 1, 2, 2, 4]
    confirm_values_are_as_expected(INDUSTRIAL, required_values)


def test_player_mat_creator_builds_engineering_as_instructed():
    required_values = [PRODUCE, TRADE, BOLSTER, MOVE, 3, 1, 2, 4, 2, 0, 3, 2, 3, 3, 1, 1, 2, 2, 2, 5]
    confirm_values_are_as_expected(ENGINEERING, required_values)


def test_player_mat_creator_builds_militant_as_instructed():
    required_values = [BOLSTER, MOVE, PRODUCE, TRADE, 3, 2, 0, 3, 1, 3, 4, 1, 1, 3, 2, 2, 3, 2, 3, 4]
    confirm_values_are_as_expected(MILITANT, required_values)


def test_player_mat_creator_builds_patriotic_as_instructed():
    required_values = [MOVE, BOLSTER, TRADE, PRODUCE, 2, 0, 1, 4, 3, 3, 4, 2, 0, 3, 1, 2, 4, 2, 2, 6]
    confirm_values_are_as_expected(PATRIOTIC, required_values)


def test_player_mat_creator_builds_innovative_as_instructed():
    required_values = [TRADE, PRODUCE, BOLSTER, MOVE, 3, 0, 3, 3, 1, 1, 4, 3, 2, 4, 2, 0, 5, 2, 3, 5]
    confirm_values_are_as_expected(INNOVATIVE, required_values)


def test_player_mat_creator_builds_mechanical_as_instructed():
    required_values = [TRADE, BOLSTER, MOVE, PRODUCE, 3, 1, 0, 3, 2, 2, 3, 1, 2, 4, 2, 2, 6, 2, 3, 6]
    confirm_values_are_as_expected(MECHANICAL, required_values)


def test_player_mat_creator_builds_agricultural_as_instructed():
    required_values = [MOVE, TRADE, PRODUCE, BOLSTER, 2, 0, 1, 4, 2, 0, 4, 2, 2, 3, 2, 3, 7, 2, 4, 7]
    confirm_values_are_as_expected(AGRICULTURAL, required_values)
