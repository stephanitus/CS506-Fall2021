import pytest
import random

from cs506 import matrix

def test_determinant():
    assert matrix.get_determinant([[4,-3],[3,-5]]) == -11
    assert matrix.get_determinant([[1,3,2],[-3,-1,-3],[2,3,1]]) == -15

