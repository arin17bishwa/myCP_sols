from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        arr = []
        n, m = len(grid), len(grid[0])
        for i in range(n):
            arr.extend(sorted(grid[i], reverse=True)[: limits[i]])
        return sum(sorted(arr, reverse=True)[:k])
