from shapes_client.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_init_positive_sides(self):
        rectangle = Rectangle(2, 5)
        result = rectangle.sides
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 5)
        self.assertEqual(result[2], 2)
        self.assertEqual(result[3], 5)

    def test_init_zero_side(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 4)

    def test_init_negative_side(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(3, -4)

    def test_set_positive_side(self):
        rectangle = Rectangle(3, 4)
        rectangle.set_side(0, 5)
        result = rectangle.sides
        self.assertEqual(result[0], 5)
        self.assertEqual(result[1], 4)
        self.assertEqual(result[2], 5)
        self.assertEqual(result[3], 4)

    def test_set_side_to_index_out_of_range(self):
        rectangle = Rectangle(3, 4)
        with self.assertRaises(ValueError):
            rectangle.set_side(-1, 5)
        with self.assertRaises(ValueError):
            rectangle.set_side(4, 5)

    def test_set_zero_side(self):
        rectangle = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            rectangle.set_side(1, 0)

    def test_set_negative_side(self):
        rectangle = Rectangle(2, 5)
        with self.assertRaises(ValueError):
            rectangle.set_side(1, -2)

    def test_get_area(self):
        rectangle = Rectangle(3, 4)
        result = rectangle.get_area()
        result = abs(result - 12)
        self.assertGreater(0.000000000001, result)

    def test_get_perimeter(self):
        rectangle = Rectangle(3, 4)
        result = rectangle.get_perimeter()
        result = abs(result - 14)
        self.assertGreater(0.000000000001, result)

    def test_is_square(self):
        rectangle = Rectangle(5, 5)
        self.assertTrue(rectangle.is_square())

    def test_is_not_square(self):
        rectangle = Rectangle(3, 4)
        self.assertFalse(rectangle.is_square())


if __name__ == '__main__':
    unittest.main()
