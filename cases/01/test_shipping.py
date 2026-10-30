from shipping import shipping_fee


def test_free_above():
    assert shipping_fee(6000) == 0


def test_free_at_boundary():
    assert shipping_fee(5000) == 0


def test_paid_just_below():
    assert shipping_fee(4999) == 500


def test_paid_small():
    assert shipping_fee(1000) == 500
