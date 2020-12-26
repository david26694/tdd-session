from src.fizzbuzz import fizzbuzz


def test_return_2():
    assert fizzbuzz(2) == 2

def test_return_3():
    assert fizzbuzz(3) == "Fizz"