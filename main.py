def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    check_matrix_param(matrix)
    return determinant_recursive(matrix)


def determinant_recursive(matrix: list[list[int]]) -> int:
    if len(matrix) == 1:
        return matrix[0][0]

    determinant = 0
    for col_num in range(len(matrix)):
        submatrix = []
        for i in range(1, len(matrix)):
            new_row = []
            for j in range(len(matrix)):
                if j != col_num:
                    new_row.append(matrix[i][j])
            submatrix.append(new_row)
        determinant += (
            (-1) ** (col_num)
            * matrix[0][col_num]
            * determinant_recursive(submatrix)
        )
    return determinant


def check_matrix_param(matrix: list[list[int]]):
    if type(matrix) is not list:
        raise Exception("Матрица должна являться списком.")
    if len(matrix) == 0:
        raise Exception("Матрица не должна быть пустой.")
    for row in matrix:
        if type(row) is not list:
            raise Exception("Строка должна быть списком.")
        if len(row) != len(matrix):
            raise Exception(
                "Матрица должна быть квадратной. "
                "Количество строк должно быть равно количеству столбцов."
            )
        for el in row:
            if type(el) is not int:
                raise Exception("Элементы матрицы должны быть целыми числами.")


def main():
    matrix = [[1, 2], [3, 4]]

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")

    print("Матрица")
    for row in matrix:
        print(row)


if __name__ == "__main__":
    main()
