import pytest
import source.my_functions as my_functions

def test_add():
	result = my_functions.add(1, 3)
	assert result == 4


def test_add_strings():
	result = my_functions.add('say my ', 'name')
	assert result == 'say my name'

def test_divide(): 
	result = my_functions.divide(10, 2)
	assert result == 5


def test_divide_by_zero(): 
	with pytest.raises(ValueError): 
		my_functions.divide(10, 0)
