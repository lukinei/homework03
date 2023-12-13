from src.square import Square


def test_square_positive():
    square = Square(3)
    assert square.calculate_area() == 9

def test_rectangle_negative():
    square = Square(0)
    assert square.calculate_area() == 9

