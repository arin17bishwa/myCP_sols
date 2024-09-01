from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        ans = [[0] * n for _ in range(m)]
        for idx, ele in enumerate(original):
            ans[idx // n][idx % n] = ele
        return ans
