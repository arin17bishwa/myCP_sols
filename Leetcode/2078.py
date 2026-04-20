from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans: int = 0
        first, last = colors[0], colors[-1]
        n = len(colors)

        for idx, color in enumerate(colors):
            ans = max(
                ans, 0 if color == first else idx, 0 if color == last else n - idx - 1
            )

        return ans
