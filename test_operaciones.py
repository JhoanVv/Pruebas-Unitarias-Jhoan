# test_operaciones.py

import pytest

from operaciones import suma, resta, multiplicacion, division

def test_suma():
    assert suma(1, 2) == 3
    assert suma(-1, -2) == -3

def test_resta():
    assert resta(5, 3) == 2
    assert resta(-5, -3) == -2

def test_multiplicacion():
    assert multiplicacion(3, 4) == 12
    assert multiplicacion(-3, -4) == 12

def test_division():
    assert division(10, 2) == 5
    assert division(-10, -2) == 5
    with pytest.raises(ValueError):
        division(10, 0)

