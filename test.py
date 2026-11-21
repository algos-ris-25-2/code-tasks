import random
import unittest

from sympy.combinatorics import GrayCode

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

    def test_string_literal(self):
        """Проверяет, что функция выбрасывает исключение при передаче строки"""
        self.assertRaises(Exception, gray_code, "5")

    def test_negative_number(self):
        """Проверяет, что функция выбрасывает исключение при отрицательном n"""
        self.assertRaises(Exception, gray_code, -10)

    def test_list_input(self):
        """Проверяет, что функция выбрасывает исключение при передаче списка"""
        self.assertRaises(Exception, gray_code, [3])

    def test_float_input(self):
        """Проверяет, что функция выбрасывает исключение при передаче дробного числа"""
        self.assertRaises(Exception, gray_code, 1.05)

    def test_false(self):
        """Проверяет, что функция выбрасывает исключение при передаче False"""
        self.assertRaises(Exception, gray_code, False)

    def test_true(self):
        """Проверяет, что функция выбрасывает исключение при передаче True"""
        self.assertRaises(Exception, gray_code, True)

    def test_no_arguments(self):
        """Проверяет, что функция выбрасывает исключение при передаче 0 аргументов"""
        self.assertRaises(TypeError, gray_code)

    def test_two_arguments(self):
        """Проверяет, что функция выбрасывает исключение при передаче 2 аргументов"""
        self.assertRaises(TypeError, gray_code, 1, 2)

    def test_random_number(self):
        """Проверяет случайные значения n от 4 до 20"""
        for _ in range(5):
            n = random.randint(4, 20)
            codes = GrayCode(n).generate_gray()
            # codes - генератор строк. Каждая строка разбивается
            # посимвольно, каждый символ (bit) преобразовывается
            # в тип int и добавляется в список
            expected = [[int(bit) for bit in item] for item in codes]
            self.assertEqual(gray_code(n), expected)

    def count_bit_differences(self, code1: list[int], code2: list[int]) -> int:
        """Вспомогательная функция для подсчета различающихся позиций в двух кодах"""
        differences = 0
        for bit1, bit2 in zip(code1, code2):
            if bit1 != bit2:
                differences += 1
        return differences

    def test_one_bit_difference(self):
        """Проверяет, что соседние коды отличаются ровно на 1 бит"""
        for _ in range(5):
            n = random.randint(2, 20)
            codes = gray_code(n)

            for i in range(len(codes) - 1):
                difference = self.count_bit_differences(codes[i], codes[i + 1])
                self.assertEqual(difference, 1)

            first_last_difference = self.count_bit_differences(codes[0], codes[-1])
            self.assertEqual(first_last_difference, 1)

    def test_codes_count(self):
        """Проверяет, что количество выводимых кодов равно 2^n"""
        for _ in range(5):
            n = random.randint(2, 20)
            codes = gray_code(n)
            self.assertEqual(len(codes), 2**n)

    def test_unique_codes(self):
        """Проверяет, что все коды уникальны"""
        for _ in range(5):
            n = random.randint(4, 20)
            codes = gray_code(n)
            unique_codes = {tuple(item) for item in codes}
            self.assertEqual(len(unique_codes), len(codes))


if __name__ == "__main__":
    unittest.main()
