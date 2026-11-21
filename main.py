def check_order(matrix):
    if len(matrix) < 1:
        raise ValueError("Порядок матрицы должен быть не менее 1")


def check_square(matrix):
    n = len(matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) != n:
            raise ValueError("Матрица не квадратная")


def check_elements(matrix):
    for row in matrix:
        for element in row:
            if not isinstance(element, int) or isinstance(element, bool):
                raise TypeError("Элементы матрицы должны быть целыми числами")


def check_tridiagonal(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise ValueError("Матрица не трёхдиагональная")


def check_diagonals(matrix):
    n = len(matrix)

    for i in range(n):
        if matrix[i][i] != matrix[0][0]:
            raise ValueError("На главной диагонали разные числа")

        if i < n - 1:
            if matrix[i][i + 1] != matrix[0][1]:
                raise ValueError("На верхней диагонали разные числа")

            if matrix[i + 1][i] != matrix[1][0]:
                raise ValueError("На нижней диагонали разные числа")


def determinant_and_previous(n: int, a: int, b: int, c: int) -> tuple[int, int]:
    if n == 1:
        return a, 1
    previous_determinant, determinant_before_previous = determinant_and_previous(
        n - 1, a, b, c
    )
    return (
        a * previous_determinant - b * c * determinant_before_previous,
        previous_determinant,
    )


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной ленты разложением.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    if matrix is None or not isinstance(matrix, list):
        raise TypeError("Матрица должна быть списком")

    check_order(matrix)
    check_square(matrix)
    check_elements(matrix)
    check_tridiagonal(matrix)
    check_diagonals(matrix)

    n = len(matrix)
    a = matrix[0][0]
    b = matrix[0][1] if n > 1 else 0
    c = matrix[1][0] if n > 1 else 0
    determinant, _ = determinant_and_previous(n, a, b, c)
    return determinant


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
