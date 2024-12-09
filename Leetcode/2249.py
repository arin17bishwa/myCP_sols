from typing import List, Set


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        def point_in_circle(x: int, y: int) -> bool:
            for circle in circles:
                if pow(circle[0] - x, 2) + pow(circle[1] - y, 2) <= pow(circle[2], 2):
                    return True
            return False

        ans = 0
        for px in range(201):
            for py in range(201):
                ans += point_in_circle(px, py)
        return ans
