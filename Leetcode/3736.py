from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        sm = mx = 0
        for ele in arr:
            mx = max(mx, ele)
            sm += ele
        return n * mx - sm
