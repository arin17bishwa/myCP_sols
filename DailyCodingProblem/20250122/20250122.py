from math import gcd, ceil
from typing import Iterable


class Fraction:
    def __init__(self, a: int, b: int):
        self.numerator = a
        self.denominator = b

    def __sub__(self, other: "Fraction"):
        lcm = (self.denominator * other.denominator) // gcd(
            self.denominator, other.denominator
        )
        _a1 = self.numerator * (lcm // self.denominator)
        _a2 = other.numerator * (lcm // other.denominator)

        new_obj = Fraction(_a1 - _a2, lcm)
        new_obj.reduce_self()
        return new_obj

    def reduce_self(self):
        self.numerator, self.denominator = self.reduce(self.numerator, self.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __bool__(self):
        return bool(self.numerator)

    @staticmethod
    def reduce(a: int, b: int) -> tuple[int, int]:
        hcf = gcd(a, b)
        return a // hcf, b // hcf


def func(a: int, b: int) -> Iterable[str]:
    ans: list[Fraction] = []
    original = Fraction(a, b)
    rem = original

    while rem:
        new_frac = Fraction(1, ceil(rem.denominator / rem.numerator))
        ans.append(new_frac)
        rem -= new_frac
    return map(str, ans)


def auto():
    pass


def main():
    a, b = 4, 13

    ans = func(a, b)

    print(*ans, sep=" + ")


if __name__ == "__main__":
    main()
