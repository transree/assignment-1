from address import normalize_zip


def test_plain():
    assert normalize_zip("1234567") == "123-4567"


def test_full_width():
    assert normalize_zip("１２３４５６７") == "123-4567"


def test_with_mark():
    assert normalize_zip("〒123-4567") == "123-4567"


def test_spaces():
    assert normalize_zip(" 123-4567 ") == "123-4567"


def test_hyphen():
    assert normalize_zip("123-4567") == "123-4567"
