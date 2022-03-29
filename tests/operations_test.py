"""Testing the calculator operations """

from calculator.Operations import Addition, Subtraction, Multiplication, Division


def test_calculator_operations_add():
    assert Addition.add(3, 1) == 4
    assert Addition.add(1, 10) == 11


def test_calculator_operations_subtract():
    assert Subtraction.subtract(6, 4) == 2


def test_calculator_operations_multiply():
    assert Multiplication.multiply(4, 4) == 16


def test_calculator_operations_divide():
    assert Division.divide(10, 2) == 5