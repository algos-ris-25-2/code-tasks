import unittest

from main import get_tridiagonal_determinant


class TestTridiagonalDeterminant(unittest.TestCase):
    """Набор тестов для проверки функции вычисления определителя
    трёхдиагональной ленточной матрицы"""

    def test_none(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр значения None"""
        self.assertRaises(Exception, get_tridiagonal_determinant, None)

    def test_not_matrix_text(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр значения matrix"""
        self.assertRaises(Exception, get_tridiagonal_determinant, "matrix")

    def test_not_matrix_int(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр числа 52"""
        self.assertRaises(Exception, get_tridiagonal_determinant, int(52))

    def test_empty_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр пустого списка"""
        self.assertRaises(Exception, get_tridiagonal_determinant, [])

    def test_row_not_list(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр матрицы, в которой одна из строк не является списком"""
        self.assertRaises(Exception, get_tridiagonal_determinant, [[1, 2], ''])

    def test_not_int_in_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметре матрицу, в которой находится не целое число"""
        matrix = [[1, 2], [3, ""]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_not_square_rectangle(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр прямоугольной матрицы"""
        matrix = [[1, 2, 0, 0], [3, 1, 2, 0], [0, 3, 1, 2]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_not_tridiag_replace_zero(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы с ненулевым элементом вне трёх диагоналей"""
        matrix = [[1, 2, 0, 7], [3, 1, 2, 0], [0, 3, 1, 2], [0, 0, 3, 1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_not_tridiag_replace_a(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы с разными элементами на главной диагонали"""
        matrix = [[1, 2, 0, 0], [3, 8, 2, 0], [0, 3, 1, 2], [0, 0, 3, 1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_not_tridiag_replace_c(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы с разными элементами на диагонали под главной диагональю"""
        matrix = [[1, 2, 0, 0], [3, 1, 2, 0], [0, 9, 1, 2], [0, 0, 3, 1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_not_tridiag_replace_b(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы с разными элементами на диагонали над главной диагональю"""
        matrix = [[1, 2, 0, 0], [3, 1, 2, 0], [0, 3, 1, 6], [0, 0, 3, 1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_first_order(self):
        """Проверяет расчет определителя для матрицы порядка 1"""
        matrix = [[1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 1)

    def test_second_order(self):
        """Проверяет расчет определителя для матрицы порядка 2"""
        matrix = [[1, 2], [2, 1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), -3)

    def test_third_order(self):
        """Проверяет расчет определителя для матрицы порядка 3"""
        matrix = [[1, -2, 0], [-4, 1, -2], [0, -4, 1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), -15)

    def test_fourth_order(self):
        """Проверяет расчет определителя для матрицы порядка 4"""
        matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 421)

    def test_tenth_order(self):
        """Проверяет расчет определителя для матрицы порядка 10"""
        matrix = [
            [-8, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, -8, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 3, -8, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, -8, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 3, -8, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, -8, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, -8, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 3, -8, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 3, -8, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 3, -8],
        ]
        self.assertEqual(get_tridiagonal_determinant(matrix), 402283936)


if __name__ == "__main__":
    unittest.main()
