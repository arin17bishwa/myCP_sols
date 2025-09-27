from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def shoelace_formula(p1: list[int], p2: list[int], p3: list[int]) -> float:
            return 0.5 * abs(
                p1[0] * (p2[1] - p3[1])
                + p2[0] * (p3[1] - p1[1])
                + p3[0] * (p1[1] - p2[1])
            )

        ans = 0
        n = len(points)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    ans = max(ans, shoelace_formula(points[i], points[j], points[k]))
        return ans
