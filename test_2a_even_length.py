import pytest
from find_unique import find_unique_element

# fehler entsteht bei gerader elementanzahl
def test_raises_value_error_on_even_length():
    with pytest.raises(ValueError):
        find_unique_element([1,2,1,2])