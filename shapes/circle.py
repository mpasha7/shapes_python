import math
from shapes.shape import Shape


class Circle(Shape):
    def __init__(self, rad: float) -> None:
        '''Инициирует экземпляр круга по его радиусу'''
        self.__radius = None
        try:
            self.radius = rad
        except ValueError as e:
            raise e

    @property
    def radius(self) -> float:
        '''Радиус круга'''
        return self.__radius

    @radius.setter
    def radius(self, value: float) -> None:
        '''Устанавливает радиус круга'''
        if value > 0:
            self.__radius = value
        else:
            raise ValueError("Радиус круга должен быть положительным числом")

    def get_area(self) -> float:
        '''Возвращает площадь круга'''
        return math.pi * self.radius ** 2

    def get_perimeter(self) -> float:
        '''Возвращает длину периметра круга (окружности)'''
        return 2 * math.pi * self.radius
