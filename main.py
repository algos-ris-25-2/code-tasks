from profilehooks import profile


# рекурсия
def fibonacci_rec(n: int) -> int:  # сложность: время O(2^n), память O(n)
    if n == 1 or n == 2:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


# итерации с массивом
def fibonacci_iter(n: int) -> int:  # сложность: время О(n), память O(n)
    if n == 1 or n == 2:
        return 1
    arr = [0] * (n + 1)
    arr[1] = arr[2] = 1
    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


# итерации без массива
def fibonacci(n: int) -> int:  # сложность: время O(n), память O(1)
    a = 1
    b = 1
    if n == 1 or n == 2:
        return 1
    for _ in range(3, n + 1):
        c = a + b
        a, b = b, c
    return c


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
