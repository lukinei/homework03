from src.triangle import Triangle

def test_triangle_positive():
    triangle = Triangle(3, 4, 5)
    assert triangle.calculate_area() == 6

def test_triangle_negative():
    triangle = Triangle(0, 0, 0)
    assert triangle.calculate_area() == 6