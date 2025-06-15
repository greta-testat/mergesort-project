import pytest
from find_unique import find_unique_element

# 1 element kommt nur einmal vor, und mehrere elemente sind im array
def test_typical_case():
    assert find_unique_element([1,2,3,4,3,1,2]) == 4

# array hat nur 1 elememt, element kommt also auch nur einmal vor
def test_single_element():
    assert find_unique_element([3]) == 3

# 1 element kommt nur einmal vor, und mehrere negative elemente sind im array
def test_with_negative_numbers():
    assert find_unique_element([-1, -2, -3, -2, -1]) == -3

# fehler entsteht bei falschem datentyp
def test_raises_type_error_on_non_list():
    with pytest.raises(TypeError):
        find_unique_element("keine liste")

# fehler entsteht bei gerader elementanzahl
def test_raises_value_error_on_even_length():
    with pytest.raises(ValueError):
        find_unique_element([1,2,1,2])
    
# fehler ensteht bei nicht-ganzzahligen werten
def test_raises_value_error_on_non_integer():
    with pytest.raises(ValueError):
        find_unique_element([1, 2, 2.5, 2, 1])