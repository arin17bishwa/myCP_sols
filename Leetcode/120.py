from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        for i in range(n - 2, -1, -1):
            arr = triangle[i]
            for j in range(len(arr)):
                arr[j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]
