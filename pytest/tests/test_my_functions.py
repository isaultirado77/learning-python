import pytest
import source.my_functions as my_functions
import time


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


@pytest.mark.slow
def test_slow(): 
	time.sleep(5)  # sleep for 5 seconds

	result = my_functions.divide(10, 5)
	assert result == 2

@pytest.mark.skip(reason='this feature is broken')  # skip reprecented as s on testing report
def test_broken():
	assert my_functions.add(2, 3) == 5


@pytest.mark.xfail(reason='division by zero')  # skip reprecented as x on testing report
def test_division_by_zero(): 
	my_functions.divide(2, 0)