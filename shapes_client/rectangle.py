from shapes import Polygon


class Rectangle(Polygon):
    def __init__(self, a: float, b: float) -> None:
        '''Инициирует экземпляр прямоугольника по его ширине и высоте'''
        try:
            super().__init__(a, b, a, b)
        except ValueError as e:
            raise e

    def set_side(self, index: int, value: float) -> None:
        '''Устанавливает размер заданной стороны прямоугольника'''
        if index < 0 or index >= len(self.sides):
            raise ValueError("Аргумент index вышел за пределы массива sides")
        if value <= 0:
            raise ValueError("Сторона многоугольника должна быть положительным числом")

        if index == 0 or index == 2:
            self.sides[0] = value
            self.sides[2] = value
        else:
            self.sides[1] = value
            self.sides[3] = value

    def get_area(self) -> float:
        '''Возвращает площадь прямоугольника'''
        return self.sides[0] * self.sides[1]

    def is_square(self) -> bool:
        '''Проверяет, является ли прямоугольник квадратом'''
        return abs(self.sides[0] - self.sides[1]) < 0.000000000001
