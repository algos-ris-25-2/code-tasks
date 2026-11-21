from collections import namedtuple
from random import choice

Case = namedtuple("Case", ["matrix", "det"])


def generate_matrix_and_det(order: int) -> Case:
    """Строит квадратную целочисленную матрицу заданного порядка
    с заранее известным определителем.

    Определитель получают из свойств, не вычисляя его разложением
    и не вызывая calculate_determinant.

    :param order: порядок матрицы, целое число не меньше 1
    :raises Exception: если order не является таким числом
    :return: Case с полями matrix и det
    """
    if type(order) is not int or order < 1:
        raise ValueError("Порядок матрицы должен быть целым числом не меньше 1")

    matrix = [[0] * order for _ in range(order)]
    det = 1

    for i in range(order):
        matrix[i][i] = choice([number for number in range(-5, 6) if number != 0])
        det *= matrix[i][i]

    if order > 1:
        for i, row_to_change in enumerate(matrix):
            other_rows = matrix[:i] + matrix[i + 1 :]
            row_to_add = choice(other_rows)
            factor = choice([number for number in range(-2, 3) if number != 0])

            for column in range(order):
                row_to_change[column] += factor * row_to_add[column]

    return Case(matrix=matrix, det=det)


def main():
    n = 10
    print(f"Генерация матрицы порядка {n}")
    result = generate_matrix_and_det(n)
    print("\nОпределитель сгенерированной матрицы равен", result.det)
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in result.matrix]))


if __name__ == "__main__":
    main()
