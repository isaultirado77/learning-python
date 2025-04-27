import pytest
import source.shapes as shapes


@pytest.fixture
def my_rectangle(): 
	return shapes.Rectangle(10., 20.)


@pytest.fixture
def other_rectangle():
	return shapes.Rectangle(3.2123123, 1.123213)