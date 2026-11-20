def validate_matrix(matrix: list[list[int]]) -> None:
    """Проверяет, что матрица квадратная, непустая и целочисленная."""
    if not isinstance(matrix, list) or not matrix:
        raise ValueError("Матрица должна быть непустым списком")

    order = len(matrix)

    for row in matrix:
        if not isinstance(row, list) or len(row) != order:
            raise ValueError("Матрица должна быть квадратной")

        if any(type(element) is not int for element in row):
            raise ValueError("Все элементы матрицы должны быть целыми числами")


def build_minor(matrix: list[list[int]], column: int) -> list[list[int]]:
    """Создаёт матрицу без первой строки и указанного столбца."""
    return [row[:column] + row[column + 1 :] for row in matrix[1:]]


def determinant_recursive(matrix: list[list[int]]) -> int:
    """Вычисляет определитель проверенной матрицы разложением по первой строке."""
    if len(matrix) == 1:
        return matrix[0][0]

    determinant = 0

    for column, element in enumerate(matrix[0]):
        minor = build_minor(matrix, column)
        sign = (-1) ** column
        algebraic_complement = sign * determinant_recursive(minor)
        determinant += element * algebraic_complement

    return determinant


def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    validate_matrix(matrix)
    return determinant_recursive(matrix)


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
