from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans: list[int] = [0] * (n + 1)
        ans[1] = 1

        for i in range(2, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans
