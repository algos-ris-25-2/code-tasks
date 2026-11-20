def recursive_determinant(a: int, b: int, c: int, order_matrix: int) -> int:
    if order_matrix == 0:
        return 1
    if order_matrix == 1:
        return a
    return a * recursive_determinant(a, b, c, order_matrix - 1) - b * c * recursive_determinant(a, b, c, order_matrix - 2)

def validate_tridiagonal_matrix(matrix: list[list[int]]) -> list[int]:    
    if not isinstance(matrix, list):
        raise TypeError

    order_matrix = len(matrix)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError

        if order_matrix != len(row):
            raise ValueError

        for el in row:
            if not isinstance(el, int):
                raise TypeError

    a = matrix[0][0]

    if order_matrix == 1:
        return [a, 0, 0, 1]

    b = matrix[0][1]
    c = matrix[1][0]

    for i in range(order_matrix):
        for j in range(order_matrix):
            if i == j:
                if matrix[i][j] != a:
                  raise ValueError('a')
            
            elif i + 1 == j:
                if matrix[i][j] != b:
                  raise ValueError('b')
            
            elif i == j + 1:
                if matrix[i][j] != c:
                  raise ValueError('c')

            else:
                if matrix[i][j] != 0:
                    raise ValueError
    
    return [a, b, c, order_matrix]


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной ленты разложением.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    
    a, b, c, order_matrix = validate_tridiagonal_matrix(matrix)
    
    return recursive_determinant(a, b, c, order_matrix)

def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
