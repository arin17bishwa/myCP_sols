from collections import deque


class Solution:
    def findLength(self, color: list[int], radius: list[int]) -> int:
        q = deque()
        for r, c in zip(radius, color):
            if q and q[-1] == (r, c):
                q.pop()
            else:
                q.append((r, c))
        return len(q)
