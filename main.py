def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Итеративное вычисление определителя трёхдиагональной матрицы.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    validate_triagonal_matrix(matrix)

    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    det_prev2 = 1
    det_prev1 = matrix[0][0]

    for i in range(1, n):
        elem_left = matrix[i][i - 1]
        elem_diag = matrix[i][i]

        sign_left = (-1) ** (i + (i - 1))
        minor_left = matrix[i - 1][i] * det_prev2
        cofactor_left = sign_left * minor_left

        sign_diag = (-1) ** (i + i)
        minor_diag = det_prev1
        cofactor_diag = sign_diag * minor_diag

        det_curr = (elem_left * cofactor_left) + (elem_diag * cofactor_diag)

        det_prev2 = det_prev1
        det_prev1 = det_curr

    return det_prev1


def validate_triagonal_matrix(matrix):
    if not isinstance(matrix, list):
        raise TypeError("Полученные данные не являются матрицей")

    if len(matrix) == 0:
        raise ValueError("Матрица пустая.")

    n = len(matrix)

    for i, row in enumerate(matrix):
        if not isinstance(row, list):
            raise TypeError("Полученные данные не являются матрицей")

        if len(row) != n:
            raise ValueError("Матрица не является кввадратной")

        for j, val in enumerate(row):
            if isinstance(val, bool) or not isinstance(val, (int, float)):
                raise TypeError(f"Элемент [{i}][{j}] не является числом")

            if abs(i - j) > 1 and val != 0:
                raise ValueError("Матрица не является трехдиагональной")

    return True


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
