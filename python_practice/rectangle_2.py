from rectangle import Rectangle, Square, Circle

# далее создаем два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
square_1 = Square(5)
square_2 = Square(10)
circle_1 = Circle(1)
circle_2 = Circle(2)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(rect_1==rect_2)
