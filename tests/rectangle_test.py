from src.rectangle import Rectangle


def test_rectangle_positive():
    rectangle = Rectangle(3, 5)
    assert rectangle.calculate_area() == 15

def test_rectangle_negative():
    rectangle = Rectangle(0, 0)
    assert rectangle.calculate_area() == 15

