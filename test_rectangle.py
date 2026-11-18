
import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    # Тесты площади
    def test_area_normal(self):
        self.assertEqual(area(5, 10), 50)

    def test_area_zero_width(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_zero_length(self):
        self.assertEqual(area(0, 10), 0)

    def test_area_square(self):
        self.assertEqual(area(5, 5), 25)

    def test_area_fractional(self):
        self.assertEqual(area(2.5, 4), 10.0)

    def test_area_small_numbers(self):
        self.assertAlmostEqual(area(0.1, 0.2), 0.02)

    def test_area_large_numbers(self):
        self.assertEqual(area(1000, 2000), 2000000)

    def test_area_one_by_one(self):
        self.assertEqual(area(1, 1), 1)

    def test_area_integer_and_float(self):
        self.assertEqual(area(3, 2.5), 7.5)

    def test_area_both_floats(self):
        self.assertAlmostEqual(area(1.5, 2.5), 3.75)

    def test_area_very_small(self):
        self.assertAlmostEqual(area(0.001, 0.001), 0.000001)

    def test_area_large_and_small(self):
        self.assertEqual(area(1000000, 0.5), 500000)

    def test_area_zero_both(self):
        self.assertEqual(area(0, 0), 0)

    def test_area_decimal_result(self):
        self.assertAlmostEqual(area(3.3, 2), 6.6)

    def test_area_different_values(self):
        self.assertEqual(area(7, 8), 56)

    # Тесты периметра
    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 10), 30)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(5, 5), 20)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_zero_width(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_zero_length(self):
        self.assertEqual(perimeter(0, 10), 20)

    def test_perimeter_fractional(self):
        self.assertEqual(perimeter(2.5, 4), 13.0)

    def test_perimeter_small_numbers(self):
        self.assertAlmostEqual(perimeter(0.1, 0.2), 0.6)

    def test_perimeter_large_numbers(self):
        self.assertEqual(perimeter(1000, 2000), 6000)

    def test_perimeter_one_by_one(self):
        self.assertEqual(perimeter(1, 1), 4)

    def test_perimeter_integer_and_float(self):
        self.assertEqual(perimeter(3, 2.5), 11.0)

    def test_perimeter_both_floats(self):
        self.assertEqual(perimeter(1.5, 2.5), 8.0)

    def test_perimeter_very_small(self):
        self.assertAlmostEqual(perimeter(0.001, 0.001), 0.004)

    def test_perimeter_large_and_small(self):
        self.assertEqual(perimeter(1000000, 0.5), 2000001)

    def test_perimeter_decimal_result(self):
        self.assertAlmostEqual(perimeter(3.3, 2), 10.6)

    def test_perimeter_different_values(self):
        self.assertEqual(perimeter(7, 8), 30)


if __name__ == "__main__":
    unittest.main()
