from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        def rotate(arr: list[list[int]], times: int = 1) -> list[list[int]]:
            if times < 1:
                return arr
            n = len(arr)
            temp = [[0] * n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    temp[n - 1 - j][i] = arr[i][j]
            return rotate(temp, times - 1)

        return target in (rotate(mat, i) for i in range(4))
