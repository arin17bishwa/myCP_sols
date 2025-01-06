from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans: List[int] = []
        n = len(boxes)
        for i in range(n):
            curr = 0
            for j, ch in enumerate(boxes):
                if ch == "1":
                    curr += abs(j - i)
            ans.append(curr)
        return ans
