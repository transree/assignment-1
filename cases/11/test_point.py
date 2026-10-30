import pytest

from point import use_points


def test_use():
    assert use_points(1000, 300) == 700


def test_use_all():
    assert use_points(1000, 1000) == 0


def test_over():
    with pytest.raises(ValueError):
        use_points(100, 300)
