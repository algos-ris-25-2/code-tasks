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

    def test_first_order_negative(self):
        """Определитель матрицы 1-го порядка с отрицательным элементом"""
        matrix = [[-5]]
        self.assertEqual(get_tridiagonal_determinant(matrix), -5)

    def test_second_order_different_diagonals(self):
        """Определитель матрицы 2-го порядка с разными побочными диагоналями"""
        matrix = [[3, 4], [2, 3]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 1)

    def test_third_order_different_diagonals(self):
        """Определитель матрицы 3-го порядка с разными диагоналями"""
        matrix = [[3, 2, 0], [-1, 3, 2], [0, -1, 3]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 39)

    def test_sixth_order(self):
        """Проверяет расчет определителя трёхдиагональной матрицы шестого порядка"""
        matrix = [
            [2, 1, 0, 0, 0, 0],
            [1, 2, 1, 0, 0, 0],
            [0, 1, 2, 1, 0, 0],
            [0, 0, 1, 2, 1, 0],
            [0, 0, 0, 1, 2, 1],
            [0, 0, 0, 0, 1, 2],
        ]
        self.assertEqual(get_tridiagonal_determinant(matrix), 7)

    def test_main_diagonal_different_values(self):
        """Исключение при разных элементах главной диагонали"""
        matrix = [[1, 4, 0], [3, 2, 4], [0, 3, 1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_upper_diagonal_different_values(self):
        """Исключение при разных элементах верхней диагонали"""
        matrix = [[1, 2, 0], [3, 1, 4], [0, 3, 1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_lower_diagonal_different_values(self):
        """Исключение при разных элементах нижней диагонали"""
        matrix = [[1, 2, 0], [3, 1, 2], [5, 4, 1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_float_element(self):
        """Проверяет обработку дробного элемента"""
        matrix = [[1.5, 2], [3, 1]]
        with self.assertRaises(TypeError):
            get_tridiagonal_determinant(matrix)

    def test_string_element(self):
        """Проверяет обработку строкового элемента"""
        matrix = [[1, "hello"], [3, 1]]
        with self.assertRaises(TypeError):
            get_tridiagonal_determinant(matrix)

    def test_bool_element(self):
        """Проверяет обработку булевого элемента."""
        matrix = [[True, 2], [3, 1]]
        with self.assertRaises(TypeError):
            get_tridiagonal_determinant(matrix)

    def test_row_is_not_list(self):
        """Проверяет обработку некорректной строки матрицы."""
        matrix = [[1, 2], "hello"]
        with self.assertRaises(ValueError):
            get_tridiagonal_determinant(matrix)


if __name__ == "__main__":
    unittest.main()
