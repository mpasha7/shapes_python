from abc import ABCMeta, abstractmethod
from shapes.shape import Shape


class Polygon(Shape):
    __metaclass__ = ABCMeta

    def __init__(self, *sides) -> None:
        '''Инициирует экземпляр многоугольника по его сторонам (абстрактно)'''
        self.__sides = list()
        try:
            self.__check_sides(*sides)
            for item in sides:
                self.__sides.append(item)
        except ValueError as e:
            raise e

    @property
    def sides(self) -> list:
        '''Стороны многоугольника'''
        return self.__sides

    def set_side(self, index: int, value: float) -> None:
        '''Устанавливает размер заданной стороны многоугольника'''
        try:
            self.__check_side(index, value)
            self.__sides[index] = value
        except ValueError as e:
            raise e

    @staticmethod
    def __sum(values: list, offset: int) -> float:
        '''Возвращает сумму элементов массива без учета последних offset элементов'''
        if values is None:
            raise ValueError("Аргумент values был равен None")
        if offset < 0:
            raise ValueError("Аргумент offset не может быть отрицательным числом")

        summa: float = 0
        for i in range(0, len(values) - offset):
            summa += values[i]
        return summa

    def __check_sides(self, *sides) -> None:
        '''Проверяет возможность создания многоугольника по заданным сторонам'''
        for side in sides:
            if side <= 0:
                raise ValueError("Сторона многоугольника должна быть положительным числом")

        arr: list = sorted(sides)
        if Polygon.__sum(arr, 1) < arr[-1]:
            raise ValueError("Одна из сторон больше суммы остальных сторон")

    def __check_side(self, index: int, value: float) -> None:
        '''Проверяет возможность изменения размера стороны многоугольника'''
        if index < 0 or index >= len(self.sides):
            raise ValueError("Аргумент index вышел за пределы массива sides")
        if value <= 0:
            raise ValueError("Сторона многоугольника должна быть положительным числом")

        arr: list = self.sides.copy()
        arr[index] = value
        arr.sort()
        if Polygon.__sum(arr, 1) < arr[-1]:
            raise ValueError("Размер стороны больше суммы остальных сторон")

    @abstractmethod
    def get_area(self):
        pass

    def get_perimeter(self) -> float:
        '''Возвращает длину периметра многоугольника'''
        return Polygon.__sum(self.sides, 0)
