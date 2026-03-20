from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        mx = 10**9

        if k == 1:
            return ans

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                arr = [0] * (k * k)
                for x in range(k):
                    for y in range(k):
                        arr[k * x + y] = grid[i + x][j + y]
                        # arr.append(grid[i + x][j + y])
                arr.sort()
                curr = mx

                for idx in range(1, len(arr)):
                    if arr[idx] == arr[idx - 1]:
                        continue
                    curr = min(curr, arr[idx] - arr[idx - 1])
                ans[i][j] = curr if curr != mx else 0

        return ans
