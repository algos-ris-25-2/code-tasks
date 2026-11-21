def validate_matrix(matrix: list[list[int]]):
    if not (isinstance(matrix, list)) or not (isinstance(matrix[0], list)):
        raise Exception("Тип не соответствует типу матрицы")
    n = len(matrix)
    if n == 0:
        raise Exception("Матрица не должна быть пустой")
    if n == 1:
        return matrix
    if any(len(row) != n for row in matrix):
        raise Exception("Количество рядов матрицы должно быть равно количеству стобцов")

    return iterate_matrix_for_check(matrix)


def iterate_matrix_for_check(matrix: list[list[int]]):
    n = len(matrix)
    row_count = 0
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    for row in matrix:
        for col in row:
            if not (isinstance(col, int)):
                raise Exception("В Матрице должны быть только целочисленные значения")

        match n:
            case 2:
                if matrix[1][1] == a:
                    return matrix
            case _:
                if row_count == 0 and (
                    row[row_count] + row[row_count + 1] != a + b
                    or row.count(0) != n - 2
                ):
                    raise Exception("Неправильно введен первый ряд")
                elif (
                    row_count != 0
                    and row_count != len(matrix) - 1
                    and (
                        row[row_count - 1] + row[row_count] + row[row_count + 1]
                        != a + b + c
                        or row.count(0) != n - 3
                    )
                ):
                    print(
                        row_count,
                        row[row_count - 1] + row[row_count] + row[row_count + 1],
                        a + b + c,
                        row.count(0),
                        n - 3,
                    )
                    raise Exception("Ряды должны состоять из трех различных элементов")
                elif row_count == len(matrix) - 1 and (
                    row[row_count - 1] + row[row_count] != a + c
                    or row.count(0) != n - 2
                ):
                    raise Exception("Неправильно введен последний ряд")
        row_count += 1
    return matrix


def calculate_tridiagonal_determinant(matrix: list[list[int]], n):
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    return matrix[0][0] * calculate_tridiagonal_determinant(matrix, n - 1) - matrix[0][
        1
    ] * matrix[1][0] * calculate_tridiagonal_determinant(matrix, n - 2)


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной ленты разложением.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    validate_matrix(matrix)
    return calculate_tridiagonal_determinant(matrix, len(matrix))


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    validate_matrix(matrix)
    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
