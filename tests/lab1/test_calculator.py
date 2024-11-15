import unittest
from src.lab1.calculator import calculator


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator(2, 3, "+"), 5)

    def test_subtraction(self):
        self.assertEqual(calculator(5, 3, "-"), 2)

    def test_multiplication(self):
        self.assertEqual(calculator(4, 3, "*"), 12)

    def test_division(self):
        self.assertEqual(calculator(6, 3, "/"), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator(6, 0, "/")

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculator(6, 3, "^")

    def test_float_operations(self):
        self.assertAlmostEqual(calculator(2.5, 1.5, "+"), 4.0)
        self.assertAlmostEqual(calculator(5.5, 3.3, "-"), 2.2)

    def test_negative_numbers(self):
        self.assertEqual(calculator(-2, -3, "+"), -5)
        self.assertEqual(calculator(-5, 3, "-"), -8)


if __name__ == "__main__":
    unittest.main()
