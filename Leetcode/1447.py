from typing import List, Set, Tuple
from math import gcd


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans: Set[str] = set()

        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                reduced_numerator, reduced_denominator = self.reduce_fraction(
                    numerator, denominator
                )
                ans.add(f"{reduced_numerator}/{reduced_denominator}")
        return list(ans)

    @staticmethod
    def reduce_fraction(numerator: int, denominator: int) -> Tuple[int, int]:
        hcf = gcd(numerator, denominator)
        return numerator // hcf, denominator // hcf
