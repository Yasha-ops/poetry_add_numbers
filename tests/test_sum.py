from poetry_add_numbers import Adder

def test_add():
    adder = Adder(1, 2)
    assert adder.sum() == 3

