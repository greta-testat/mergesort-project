import pytest
from find_unique import find_unique_element

# fehler entsteht bei falschem datentyp
def test_raises_type_error_on_non_list():
    with pytest.raises(TypeError):
        find_unique_element("keine liste")