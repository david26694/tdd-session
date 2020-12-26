from src.fizzbuzz import fizzbuzz


def test_return_2():
    assert fizzbuzz(2) == 2

def test_return_3():
    assert fizzbuzz(3) == "Fizz"

def test_return_5():
    assert fizzbuzz(5) == "Buzz"

def test_return_15():
    assert fizzbuzz(15) == "FizzBuzz"