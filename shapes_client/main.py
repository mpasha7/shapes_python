from shapes import Circle, Polygon, Triangle
from rectangle import Rectangle


def use_shapes():
    shapes_list = [
        Circle(1),
        Triangle(3, 4, 3),
        Rectangle(3, 5)              ## Пример класса, наследованного от библиотечного
    ]

    for shape in shapes_list:
        print("Периметр:", shape.get_perimeter())  ## Вычисление площади и периметра без знания типа фигуры
        print("Площадь:", shape.get_area())
        if isinstance(shape, Circle):
            print("Радиус:", shape.radius)
            shape.radius = 2
            print("\nНовый радиус:", shape.radius)
        elif isinstance(shape, Polygon):
            print("Стороны:", shape.sides)
            if isinstance(shape, Triangle):
                print("Это прямоугольный треугольник?:", shape.is_right())
            elif isinstance(shape, Rectangle):
                print("Это квадрат?:", shape.is_square())

            shape.set_side(0, 5)
            print("\nНовые стороны:", shape.sides)
            if isinstance(shape, Triangle):
                print("А теперь прямоугольный треугольник?:", shape.is_right())
            elif isinstance(shape, Rectangle):
                print("А теперь квадрат?:", shape.is_square())

        print("Новый периметр:", shape.get_perimeter())
        print("Новая площадь:", shape.get_area())
        print("-" * 30)


if __name__ == "__main__":
    use_shapes()