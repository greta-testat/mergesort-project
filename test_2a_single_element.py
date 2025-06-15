import pytest
from find_unique import find_unique_element

# array hat nur 1 elememt, element kommt also auch nur einmal vor
def test_single_element():
    assert find_unique_element([3]) == 3