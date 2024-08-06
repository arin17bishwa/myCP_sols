from typing import List, Tuple
from math import gcd


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans: List[str] = []

        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                reduced_numerator, reduced_denominator = self.reduce_fraction(
                    numerator, denominator
                )
                if reduced_denominator == denominator:
                    ans.append(f"{reduced_numerator}/{reduced_denominator}")
        return ans

    @staticmethod
    def reduce_fraction(numerator: int, denominator: int) -> Tuple[int, int]:
        hcf = gcd(numerator, denominator)
        return numerator // hcf, denominator // hcf
