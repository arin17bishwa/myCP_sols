from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans: List[int] = [0] * n
        lhs_balls = lhs_moves = 0
        rhs_balls = rhs_moves = 0

        for i in range(1, n):
            lhs_balls += boxes[i - 1] == "1"
            lhs_moves += lhs_balls
            ans[i] = lhs_moves

        for i in range(n - 2, -1, -1):
            rhs_balls += boxes[i + 1] == "1"
            rhs_moves += rhs_balls
            ans[i] += rhs_moves
        return ans
