from order_number import next_order_number


def test_first_number():
    assert next_order_number() == "A00001"
