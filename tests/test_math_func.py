from nis import match
from src import math_func
import pytest

def test_add():
    assert math_func.add(3, 7) == 10
    assert math_func.add(7) == 9
    