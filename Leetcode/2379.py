from typing import List


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s = blocks
        n = len(s)
        cost: List[int] = [0] + [int(i == "W") for i in s]

        for i in range(1, n + 1):
            cost[i] += cost[i - 1]

        return min(cost[i] - cost[i - k] for i in range(k, n + 1))
