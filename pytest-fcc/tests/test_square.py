import pytest
import source.shapes as shapes

@pytest.mark.parametrize('side, expected_area', [(5, 25), (4, 16), (9, 81)])
def test_multiple_areas(side, expected_area): 
    assert shapes.Square(side).area() == expected_area


