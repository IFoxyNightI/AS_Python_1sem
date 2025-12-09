if __name__ == "__main__":
    pass
def gcd(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return abs(a)

def reduce_fraction(numerator: int, denominator: int) -> tuple:
    if denominator == 0:
        raise ValueError("Знаменатель не может быть равен нулю")
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor


def fraction_to_decimal(numerator: int, denominator: int, precision: int = 6) -> float:
    if denominator == 0:
        raise ValueError("Знаменатель не может быть равен нулю")
    return round(numerator / denominator, precision)

# Пример
import fraction_module as fm

num, den = 16, 64

print(f"   Исходная дробь: {num}/{den}")

# Находим НОД
g = fm.gcd(num, den)
print(f"   Шаг 1: НОД = {g}")

# Сокращаем дробь
red_num, red_den = fm.reduce_fraction(num, den)
print(f"   Шаг 2: Сокращенная дробь = {red_num}/{red_den}")

# Переводим в десятичную
decimal_value = fm.fraction_to_decimal(num, den)
print(f"   Шаг 3: Десятичное значение = {decimal_value}")
