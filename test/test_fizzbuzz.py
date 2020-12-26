from src.fizzbuzz import fizzbuzz
import pytest 

@pytest.mark.parametrize(
    "input,output",
    [(2, 2), (3, 'Fizz'), (5, 'Buzz'), (15, 'FizzBuzz'), (30, 'FizzBuzz')]
    )
def test_io(input, output):
    assert fizzbuzz(input) == output

