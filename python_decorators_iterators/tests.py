import unittest

from playground import multiply_by_5, divide_50_by


class TestPlayground(unittest.TestCase):
    def test_multiply_by_5_with_5_returns_25(self):
        result = multiply_by_5(5)
        expected_result = 25
        self.assertEqual(result, expected_result)

    def test_multiply_by_5_with_10_returns_50(self):
        self.assertEqual(multiply_by_5(10), 50)

    def test_multiply_by_5_with_int_text_2_returns_10(self):
        self.assertEqual(multiply_by_5("2"), 10)

    def test_multiply_by_5_with_text_raises_error(self):
        with self.assertRaises(ValueError):
            multiply_by_5("hello")


class TestDivide50By(unittest.TestCase):
    def test_divide_50_by_0_return_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide_50_by(0)

    def test_divide_50_by_10_return_5(self):
        self.assertEqual(divide_50_by(10), 5)

    def test_divide_50_by_05_return_100(self):
        self.assertEqual(divide_50_by(0.5), 100)


if __name__ == "__main__":
    unittest.main()
