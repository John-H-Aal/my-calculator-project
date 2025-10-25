"""
Tests for Calculator klassen
"""
import pytest
from my_calculator.calculator import Calculator


def test_add():
    """Test addition"""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0


def test_subtract():
    """Test subtraktion"""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 1) == 0
    assert calc.subtract(0, 5) == -5


def test_multiply():
    """Test multiplikation"""
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 5) == 0
    assert calc.multiply(-2, 3) == -6


def test_divide():
    """Test division"""
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3
    

def test_divide_by_zero():
    """Test at division med nul giver fejl"""
    calc = Calculator()
    with pytest.raises(ValueError, match="Kan ikke dividere med nul!"):
        calc.divide(5, 0)
