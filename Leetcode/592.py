from math import gcd
import re


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def sum(self, other: "Fraction") -> "Fraction":
        den_lcm = (self.denominator * other.denominator) // gcd(
            self.denominator, other.denominator
        )
        total_num = (self.numerator * (den_lcm // self.denominator)) + (
            other.numerator * (den_lcm // other.denominator)
        )
        fraction_gcd = gcd(total_num, den_lcm)
        self.numerator = total_num // fraction_gcd
        self.denominator = den_lcm // fraction_gcd
        return self

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = re.split("/|(?=[-+])", expression)
        nums = list(filter(None, nums))
        fractions = []
        for i in range(0, len(nums), 2):
            fractions.append(
                Fraction(numerator=int(nums[i]), denominator=int(nums[i + 1]))
            )
        ans = fractions[0]
        for fraction in fractions[1:]:
            ans.sum(fraction)
        return str(ans)


if __name__ == "__main__":
    obj = Solution()
    exp = "-1/2+1/2+1/3"
    print(obj.fractionAddition(exp))
