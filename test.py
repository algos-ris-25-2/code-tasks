import unittest

from main import get_tridiagonal_determinant


class TestTridiagonalDeterminant(unittest.TestCase):
    """Набор тестов для проверки функции вычисления определителя
    трёхдиагональной ленточной матрицы"""

    def test_none(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр значения None"""
        self.assertRaises(Exception, get_tridiagonal_determinant, None)

    def test_empty_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр пустого списка"""
        self.assertRaises(Exception, get_tridiagonal_determinant, [])

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

class TestTridiagonalDeterminantAdditionalCases(unittest.TestCase):
    """Дополнительные тесты."""

    def test_invalid_type_string(self):
        """Проверяет, что функция выбрасывает исключение при передаче строки
        вместо матрицы"""
        self.assertRaises(Exception, get_tridiagonal_determinant, "matrix")

    def test_invalid_type_int(self):
        """Проверяет, что функция выбрасывает исключение при передаче числа
        вместо матрицы"""
        self.assertRaises(Exception, get_tridiagonal_determinant, 123)

    def test_nested_tuple_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче матрицы
        из неизменяемых списков"""
        self.assertRaises(Exception, get_tridiagonal_determinant, ((1, 0), (0, 1)))

    def test_row_not_list(self):
        """Проверяет, что функция выбрасывает исключение, если строка матрицы
        не является списком"""
        self.assertRaises(Exception, get_tridiagonal_determinant, [[1, 0], (0, 1)])

    def test_bool_true_element(self):
        """Проверяет, что функция выбрасывает исключение при наличии булева
        значения в матрице"""
        self.assertRaises(Exception, get_tridiagonal_determinant, [[True]])

    def test_bool_false_element(self):
        """Проверяет, что функция выбрасывает исключение при наличии булева
        значения в матрице"""
        self.assertRaises(Exception, get_tridiagonal_determinant, [[False]])

    def test_negative_first_order(self):
        """Проверяет расчёт определителя для матрицы порядка 1 с отрицательным
        элементом"""
        self.assertEqual(get_tridiagonal_determinant([[-67]]), -67)

    def test_triangular_matrices(self):
        """Проверяет расчёт определителя для треугольных матриц"""
        matrix_1 = [[2, 0, 0, 0], [4, 2, 0, 0], [0, 4, 2, 0], [0, 0, 4, 2]]
        matrix_2 = [[-6, 7, 0], [0, -6, 7], [0, 0, -6]]
        self.assertEqual(get_tridiagonal_determinant(matrix_1), 16)
        self.assertEqual(get_tridiagonal_determinant(matrix_2), -216)

    def test_zero_main_diagonal_parity(self):
        """Проверяет расчёт определителя для матрицы с нулевой главной
        диагональю"""
        matrix_1 = [[0, 2, 0, 0], [4, 0, 2, 0], [0, 4, 0, 2], [0, 0, 4, 0]]
        matrix_2 = [[0, 7, 0], [6, 0, 7], [0, 6, 0]]
        self.assertEqual(get_tridiagonal_determinant(matrix_1), 64)
        self.assertEqual(get_tridiagonal_determinant(matrix_2), 0)

if __name__ == "__main__":
    unittest.main()
