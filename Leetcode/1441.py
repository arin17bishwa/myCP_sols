from collections import deque
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        t = deque(target)
        ans: list[str] = []
        for i in range(1, 1 + n):
            if t:
                ans.append("Push")

                if t[0] != i:
                    ans.append("Pop")
                else:
                    t.popleft()
            else:
                break
        return ans
