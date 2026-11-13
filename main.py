from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n == 0:
        return 0
    if n <= 2:
        return 1  # Если элементов 1 или 2 то они = 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n == 0:
        return 0  # Если элементов нет то возвращаем 0

    array = [1, 1]  # Создаем массив с первыми двумя числами

    for i in range(2, n):
        array.append(
            array[i - 1] + array[i - 2]
        )  # Каждый следующий элемент равен сумме 2 предыдущих
    return array[-1]


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n == 0:
        return 0  # Если эллементов нет то возвращаем 0

    a, b = 1, 1

    for _ in range(2, n):
        c = a + b
        a, b = b, c
    return b

@profile()
def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()
