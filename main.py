def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """

    def calculate_determinant_rec(matrix: list[list[int]]) -> int:
        if len(matrix) == 1:
            return matrix[0][0]

        return sum(
            (-1) ** i
            * matrix[0][i]
            * calculate_determinant_rec(get_sub_matrix(matrix, i))
            for i in range(len(matrix))
        )

    def get_sub_matrix(matrix: list[list[int]], col: int) -> list[list[int]]:
        sub_matrix = []
        for row in matrix[1:]:
            new_row = row.copy()
            new_row.pop(col)
            sub_matrix.append(new_row)

        return sub_matrix

    validation(matrix)
    return calculate_determinant_rec(matrix)


def validation(matrix):
    if not isinstance(matrix, list):
        raise Exception("Матрица должна быть списком")
    if not matrix:
        raise Exception("Матрица должна состоять хотя бы из одного элемента")
    if not all(isinstance(row, list) for row in matrix):
        raise Exception("Все строки в матрице должны быть списками")
    if not all(len(row) == len(matrix) for row in matrix):
        raise Exception("Матрица должна быть квадратной")
    if not all(type(num) is int for row in matrix for num in row):
        raise Exception("Все элементы должны быть целыми числами")


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
