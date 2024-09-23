# tests/test_my_module.py
#%pip install pytest
# Import the module correctly
import sys
sys.path.append('/Workspace/Repos/ramesh.sadineni@gmail.com/azurerepo/src/my_module')  # Add the path to your module
import pytest
from src.my_module import add

def test_add():
    assert add(2, 3) == 5  # Test that 2 + 3 equals 5
    assert add(-1, 1) == 0  # Test that -1 + 1 equals 0
    assert add(0, 0) == 0   # Test that 0 + 0 equals 0

# Optional: You can use pytest to check for exceptions
def test_add_type_error():
    with pytest.raises(TypeError):
        add("two", 3)  # This should raise a TypeError because "two" is a string
