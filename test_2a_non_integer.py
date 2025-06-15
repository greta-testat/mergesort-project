import pytest
from find_unique import find_unique_element

# fehler ensteht bei nicht-ganzzahligen werten
def test_raises_value_error_on_non_integer():
    with pytest.raises(ValueError):
        find_unique_element([1, 2, 2.5, 2, 1])