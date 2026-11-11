import random

COMMON_FACTORS = 0
A_ONLY_FACTORS = 1
B_ONLY_FACTORS = 2


class GcdGenerator:
    """Генерирует пары чисел с известными НОД и НОК.

    Числа собираются из простых, возведённых в случайную степень:
    общие множители входят в оба числа, остальные не пересекаются.
    Метод generate_values заполняет внутреннее состояние,
    свойства gcd_value, a_value, b_value и lcm_value его только читают.
    """

    def __init__(self):
        self.__primes: tuple[int, ...] = (
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
        )
        """Набор простых чисел для генерации значений"""
        self.__values: list[dict] = [{}, {}, {}]
        """Сгенерированные значения, общие множители (индекс COMMON_FACTORS),
        множители исключительно для a_value (индекс A_ONLY_FACTORS),
        множители исключительно для b_value (индекс B_ONLY_FACTORS)"""
        self.generate_values()

    @property
    def gcd_value(self) -> int:
        """Возвращает значение НОД для a_value и b_value"""
        ans = 1
        for prime, power in self.__values[COMMON_FACTORS].items():
            ans *= prime**power

        return ans

    @property
    def a_value(self) -> int:
        """Возвращает число, полученное в результате перемножения простых чисел,
        возведенных в случайную степень. Число имеет как общие, так и различные
        множители с числом b_value"""
        ans = self.gcd_value
        for prime, power in self.__values[A_ONLY_FACTORS].items():
            ans *= prime**power

        return ans

    @property
    def b_value(self) -> int:
        """Возвращает число, полученное в результате перемножения простых чисел,
        возведенных в случайную степень. Число имеет как общие, так и различные
        множители с числом a_value"""
        ans = self.gcd_value
        for prime, power in self.__values[B_ONLY_FACTORS].items():
            ans *= prime**power

        return ans

    @property
    def lcm_value(self) -> int:
        """Возвращает значение НОК для a_value и b_value"""
        return self.a_value * self.b_value // self.gcd_value

    @property
    def max_factor_cnt(self) -> int:
        """Возвращает количество простых множителей, которые можно использовать
        для генерации чисел"""
        return len(self.__primes)

    def generate_values(self, factor_cnt: int = 5, max_pow: int = 5) -> None:
        """Процедура генерирует значения a_value, b_value, gcd_value и lcm_value.
        :param factor_cnt: Количество простых чисел, используемых для генерации,
        не должно превышать значение max_factor_cnt. Значение по умолчанию 5.
        :param max_pow: Верхняя граница для случайной степени. Значение по
        умолчанию 5.
        :return: None
        """
        # я немного не понимаю почему в функции задано factor_cnt почему
        # мы не рандомно берем количество простых чисел ну ладно
        factor_cnt = min(factor_cnt, self.max_factor_cnt)
        # выбираем количество простых чисел из primes
        prime_list = random.sample(self.__primes, factor_cnt)
        ans = {}
        for i in range(factor_cnt):
            power = random.randint(1, max(1, max_pow))
            ans[prime_list[i]] = power

        self.__values[COMMON_FACTORS] = ans

        primes_list_a = [x for x in self.__primes if x not in prime_list]
        count_a = random.randint(0, len(primes_list_a))
        primes_list_a = random.sample(primes_list_a, count_a)
        ans_a = {}
        for i in range(count_a):
            power = random.randint(1, max(1, max_pow))
            ans_a[primes_list_a[i]] = power

        self.__values[A_ONLY_FACTORS] = ans_a

        primes_list_b = [
            x for x in self.__primes if x not in prime_list and x not in primes_list_a
        ]
        count_b = random.randint(0, len(primes_list_b))
        primes_list_b = random.sample(primes_list_b, count_b)
        ans_b = {}
        for i in range(count_b):
            power = random.randint(1, max(1, max_pow))
            ans_b[primes_list_b[i]] = power

        self.__values[B_ONLY_FACTORS] = ans_b

        return self.__values


if __name__ == "__main__":
    print("Генерация чисел для проверки НОД/НОК")
    generator = GcdGenerator()
    values = generator.generate_values(8, 5)
    print("Число a = %d" % generator.a_value)
    print("Число b = %d" % generator.b_value)
    print("НОД(a, b) = %d" % generator.gcd_value)
    print("НОК(a, b) = %d" % generator.lcm_value)
    # print(generator.generate_values())
