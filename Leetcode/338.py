from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans: list[int] = [0] * (n + 1)
        highest_power: int = 1

        for i in range(1, n + 1):
            if (highest_power << 1) <= i:
                highest_power <<= 1

            ans[i] = ans[i - highest_power] + 1

        return ans
