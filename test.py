import unittest

from main import calculate_determinant
from matrix_generator import generate_matrix_and_det


def require_generator(test_case):
    sample = generate_matrix_and_det(1)
    if sample is None:
        test_case.skipTest("Generator is not implemented")
    return sample


class TestDeterminant(unittest.TestCase):
    """Набор тестов для проверки функции вычисления определителя
    целочисленной квадратной матрицы"""

    def test_none(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр значения None"""
        self.assertRaises(Exception, calculate_determinant, None)

    def test_empty_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр пустого списка"""
        self.assertRaises(Exception, calculate_determinant, [])

    def test_not_square_rectangle(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр прямоугольной матрицы"""
        matrix = [[3, -3, -5, 8], [-3, 2, 4, -6], [-4, 3, 5, -6]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_first_order(self):
        """Проверяет расчет определителя для матрицы порядка 1"""
        matrix = [[1]]
        self.assertEqual(calculate_determinant(matrix), 1)

    def test_second_order(self):
        """Проверяет расчет определителя для матрицы порядка 2"""
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(calculate_determinant(matrix), -2)

    def test_third_order(self):
        """Проверяет расчет определителя для матрицы порядка 3"""
        matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        self.assertEqual(calculate_determinant(matrix), 0)

    def test_fourth_order(self):
        """Проверяет расчет определителя для матрицы порядка 4"""
        matrix = [[3, -3, -5, 8], [-3, 2, 4, -6], [2, -5, -7, 5], [-4, 3, 5, -6]]
        self.assertEqual(calculate_determinant(matrix), 18)

    def test_generator(self):
        """Проверяет генератор матриц с известным определителем"""
        require_generator(self)
        for order in range(1, 11):
            with self.subTest(order=order):
                test_case = generate_matrix_and_det(order)
                self.assertEqual(len(test_case.matrix), order)
                for row in test_case.matrix:
                    self.assertEqual(len(row), order)
                self.assertEqual(calculate_determinant(test_case.matrix), test_case.det)

    def test_ragged_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы со строками разной длины"""
        matrix = [[1, 2], [3]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_generator_rejects_invalid_order(self):
        """Проверяет, что генератор выбрасывает исключение при передаче
        недопустимого порядка матрицы"""
        for order in (0, -1, True, 2.0):
            with self.subTest(order=order):
                self.assertRaises(ValueError, generate_matrix_and_det, order)

    def test_matrix_is_not_modified(self):
        """Проверяет, что вычисление определителя сохраняет
        исходную матрицу"""
        matrix = [[2, 1, 0], [3, 4, 5], [1, -1, 3]]
        original = [row.copy() for row in matrix]

        calculate_determinant(matrix)

        self.assertEqual(matrix, original)

    def test_swapping_rows_changes_sign(self):
        """Проверяет, что перестановка двух строк меняет
        знак определителя"""
        original = [[3, 1], [2, 2]]
        swapped = [[2, 2], [3, 1]]

        self.assertEqual(calculate_determinant(original), 4)
        self.assertEqual(calculate_determinant(swapped), -4)

    def test_equal_rows(self):
        """Проверяет, что определитель матрицы
        с двумя одинаковыми строками равен нулю"""
        matrix = [[2, 1, 3], [1, 4, 2], [2, 1, 3]]
        self.assertEqual(calculate_determinant(matrix), 0)


if __name__ == "__main__":
    unittest.main()
