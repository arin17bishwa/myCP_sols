from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        exp = 0
        while n:
            b = pow(10, exp)
            ans.append(b * (n % 10))
            n //= 10
            exp += 1
        return list(filter(lambda x: x, reversed(ans)))
