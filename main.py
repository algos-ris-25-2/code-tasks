def gray_code(n: int) -> list[list[int]]:
    """Проверяет входные данные и возвращает рекурсивно построенный полный n-разрядный код Грея зеркальным построением.

    :param n: число разрядов, целое не меньше 1.
        Логическое значение не является допустимой длиной
    :raises Exception: если n не является таким числом
    :return: список из 2**n слов в стандартной нумерации
    """
    validation(n)
    return _gray_code(n)

def _gray_code(n: int) -> list[list[int]]:
    """Рекурсивно строит полный n-разрядный код Грея зеркальным построением.

    :param n: проверенное значение числа разрядов, целое не меньше 1
    :return: список из 2**n слов в стандартной нумерации
    """
    if n == 1:
        return [[0], [1]]
    prev_gray_code = _gray_code(n - 1)
    result = [[0] + item for item in prev_gray_code] + [[1] + item for item in reversed(prev_gray_code)]
    return result 

def validation(n) -> bool:
    """Проверяет, что входные данные являются целым числом, которое имеет значение не менее 1 и не является логическим значением.
    
    :param n: входные данные
    :raises Exception: если n не является таким числом
    :return: True, если валидация пройдена
    """
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise Exception("n должно являться целым числом, значение которого не менее 1")
    return True
    

def main():
    n = 3
    print(f"Код Грея, число разрядов {n}")
    for word in gray_code(n):
        print(word)


if __name__ == "__main__":
    main()

