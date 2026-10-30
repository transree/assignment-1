from stock_api import fetch_stock, is_low


def test_low():
    assert is_low(3)


def test_boundary():
    assert is_low(5)


def test_fetch():
    assert fetch_stock("A-1") >= 0


def test_not_low():
    assert not is_low(10)
