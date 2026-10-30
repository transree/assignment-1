from points import points_for


def test_hundred():
    assert points_for(100) == 1


def test_round_down():
    assert points_for(199) == 1


def test_zero():
    assert points_for(99) == 0
