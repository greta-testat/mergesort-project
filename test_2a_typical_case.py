import pytest
from find_unique import find_unique_element

# 1 element kommt nur einmal vor, und mehrere elemente sind im array
def test_typical_case():
    assert find_unique_element([1,2,3,4,3,1,2]) == 4
