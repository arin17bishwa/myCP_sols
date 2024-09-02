from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)

        for idx, ele in enumerate(chalk):
            k -= ele
            if k < 0:
                return idx
        return 0
