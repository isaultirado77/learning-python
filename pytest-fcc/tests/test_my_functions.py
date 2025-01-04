import pytest
import source.my_functions as my_functions

def test_add():
	result = my_functions.add(1, 3)
	assert result == 4

