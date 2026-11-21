def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Итеративное вычисление определителя трёхдиагональной матрицы.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    validate_tridiagonal_matrix(matrix)
    
    n = len(matrix)
    a = matrix[0][0]

    if n == 1:
        return a

    b = matrix[0][1]
    c = matrix[1][0]

    bc = b * c
    det_prev = 1
    det_curr = a

    for i in range(2, n + 1):
        det_prev, det_curr = det_curr, a * det_curr - bc * det_prev

    return det_curr

def validate_tridiagonal_matrix(matrix):
    """Проверяет корректность трёхдиагональной матрицы"""
    if not isinstance(matrix, list):
        raise TypeError("Матрица должна быть списком из списков!")

    n = len(matrix)
    if n == 0:
        raise ValueError("Порядок матрицы должен быть не меньше 1!")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("Каждая строка матрицы должна быть списком!")

        if len(row) != n:
            raise ValueError("Матрица должна быть квадратной!")

        for val in row:
            if not isinstance(val, int) or isinstance(val, bool):
                raise TypeError("Все элементы матрицы должны быть целыми числами!")

    a = matrix[0][0]
    if n > 1:
        b = matrix[0][1]
        c = matrix[1][0]
    else:
        b = 0
        c = 0

    for i in range(n):
        for j in range(n):
            val = matrix[i][j]
            if i == j:
                if val != a:
                    raise ValueError(
                        "Элементы главной диагонали должны быть одинаковыми!"
                    )
            elif j == i + 1:
                if val != b:
                    raise ValueError(
                        "Элементы верхней наддиагонали должны быть одинаковыми!"
                    )
            elif i == j + 1:
                if val != c:
                    raise ValueError(
                        "Элементы нижней поддиагонали должны быть одинаковыми!"
                    )
            elif val != 0:
                raise ValueError("Элементы вне трёх диагоналей должны быть равны нулю!")

def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
