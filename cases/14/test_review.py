import pytest

from review import average, label


def test_empty():
    assert average([]) == 0


@pytest.mark.slow
def test_average():
    assert average([5, 4, 3]) == 4.0


@pytest.mark.slow
def test_label_boundary():
    assert label(4.0) == "高評価"


@pytest.mark.slow
def test_label_high():
    assert label(4.5) == "高評価"


@pytest.mark.slow
def test_label_normal():
    assert label(3.0) == "通常"
