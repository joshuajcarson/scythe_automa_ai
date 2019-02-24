from scythe_automa_ai.scythe_board_creator import ScytheBoard, IDENTIFIER, U_CORD, V_CORD


def test_board_has_home_for_saxony_in_correct_location():
    board_created = ScytheBoard()
    saxony_home_base = board_created.tiles[board_created.tiles[IDENTIFIER] == 'saxony_home_base'].iloc[0]
    assert 1 == len(board_created.tiles[board_created.tiles[IDENTIFIER] == 'saxony_home_base'])
    assert -4 == saxony_home_base.loc[U_CORD]
    assert 7 == saxony_home_base.loc[V_CORD]
