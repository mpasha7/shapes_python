from shapes import Triangle
import unittest


class TestTriangle(unittest.TestCase):
    def test_init_positive_sides(self):
        triangle = Triangle(3, 4, 5)
        result = triangle.sides
        self.assertEqual(result[0], 3)
        self.assertEqual(result[1], 4)
        self.assertEqual(result[2], 5)

    def test_init_zero_side(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(0, 4, 5)

    def test_init_negative_side(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(3, -4, -5)

    def test_init_too_big_side(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(3, 4, 8)

    def test_set_positive_side(self):
        triangle = Triangle(3, 4, 5)
        triangle.set_side(0, 5)
        result = triangle.sides
        self.assertEqual(result[0], 5)
        self.assertEqual(result[1], 4)
        self.assertEqual(result[2], 5)

    def test_set_side_to_index_out_of_range(self):
        triangle = Triangle(3, 4, 5)
        with self.assertRaises(ValueError):
            triangle.set_side(-1, 5)
        with self.assertRaises(ValueError):
            triangle.set_side(3, 5)

    def test_set_zero_side(self):
        triangle = Triangle(1, 1, 1)
        with self.assertRaises(ValueError):
            triangle.set_side(1, 0)

    def test_set_negative_side(self):
        triangle = Triangle(3, 4, 5)
        with self.assertRaises(ValueError):
            triangle.set_side(1, -2)

    def test_set_too_big_side(self):
        triangle = Triangle(3, 4, 5)
        with self.assertRaises(ValueError):
            triangle.set_side(2, 8)

    def test_get_area(self):
        triangle = Triangle(3, 4, 5)
        result = triangle.get_area()
        result = abs(result - 6)
        self.assertGreater(0.000000000001, result)

    def test_get_perimeter(self):
        triangle = Triangle(3, 4, 5)
        result = triangle.get_perimeter()
        result = abs(result - 12)
        self.assertGreater(0.000000000001, result)

    def test_is_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

    def test_is_not_right(self):
        triangle = Triangle(5, 5, 5)
        self.assertFalse(triangle.is_right())


if __name__ == '__main__':
    unittest.main()
