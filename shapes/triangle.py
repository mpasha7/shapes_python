import math
from shapes.polygon import Polygon


class Triangle(Polygon):
    def __init__(self, a: float, b: float, c: float) -> None:
        '''Инициирует экземпляр треугольника по трем его сторонам'''
        try:
            super().__init__(a, b, c)
        except ValueError as e:
            raise e

    def get_area(self) -> float:
        '''Возвращает площадь треугольника'''
        p: float = self.get_perimeter() / 2
        return math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))

    def is_right(self) -> bool:
        '''Проверяет, является ли треугольник прямоугольным'''
        arr: list = sorted(self.sides)
        return abs(arr[0] ** 2 + arr[1] ** 2 - arr[2] ** 2) < 0.000000000001
