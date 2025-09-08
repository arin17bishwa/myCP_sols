from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def is_valid(x: int) -> bool:
            return "0" not in str(x)

        for i in range(1, n + 1):
            if is_valid(i) and is_valid(n - i):
                return [i, n - i]
        return [-1, -1]
