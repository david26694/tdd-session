from src.src_sample import ceil


def test_positive_integer():
    assert ceil(7) == 7

def test_positive_decimal():
    assert ceil(7.5) == 7

def test_negative_decimal():
    assert ceil(-7.5) == -8

def test_negative_integer():
    assert ceil(-10) == -10