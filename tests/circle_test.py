from src.circle import Circle


def test_circle_positive():
    circle = Circle(2)
    assert circle.calculate_area() == 12.566370614359172

def test_circle_negative():
    circle = Circle(0)
    assert circle.calculate_area() == 12.566370614359172