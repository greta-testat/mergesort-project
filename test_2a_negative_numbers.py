import pytest
from find_unique import find_unique_element

# 1 element kommt nur einmal vor, und mehrere negative elemente sind im array
def test_with_negative_numbers():
    assert find_unique_element([-1, -2, -3, -2, -1]) == -3