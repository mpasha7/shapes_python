from shapes import Circle
import unittest
import math


class TestCircle(unittest.TestCase):
    def test_init_positive_radius(self):
        circle = Circle(1)
        result = circle.radius
        self.assertEqual(result, 1)

    def test_init_zero_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle(0)

    def test_init_negative_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle(-1)

    def test_set_positive_radius(self):
        circle = Circle(1)
        circle.radius = 2
        result = circle.radius
        self.assertEqual(result, 2)

    def test_set_zero_radius(self):
        circle = Circle(1)
        with self.assertRaises(ValueError):
            circle.radius = 0

    def test_set_negative_radius(self):
        circle = Circle(1)
        with self.assertRaises(ValueError):
            circle.radius = -1

    def test_get_area(self):
        circle = Circle(10)
        result = circle.get_area()
        result = abs(result - math.pi*100)
        self.assertGreater(0.000000000001, result)

    def test_get_perimeter(self):
        circle = Circle(10)
        result = circle.get_perimeter()
        result = abs(result - math.pi*20)
        self.assertGreater(0.000000000001, result)


if __name__ == '__main__':
    unittest.main()
