import unittest

from main import gray_code


class TestGrayCode(unittest.TestCase):
    """Набор тестов для проверки рекурсивной генерации кода Грея"""

    def test_none(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        значения None"""
        self.assertRaises(Exception, gray_code, None)

    def test_zero_length(self):
        """Проверяет, что функция выбрасывает исключение при нулевой длине"""
        self.assertRaises(Exception, gray_code, 0)

    def test_one_bit(self):
        """Проверяет код длины 1"""
        self.assertEqual(gray_code(1), [[0], [1]])

    def test_two_bits(self):
        """Проверяет код длины 2"""
        self.assertEqual(gray_code(2), [[0, 0], [0, 1], [1, 1], [1, 0]])

    def test_three_bits(self):
        """Проверяет стандартную нумерацию для длины 3"""
        expected = [
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 1],
            [0, 1, 0],
            [1, 1, 0],
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 0],
        ]
        self.assertEqual(gray_code(3), expected)


if __name__ == "__main__":
    unittest.main()
