from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = temperatures
        n = len(arr)
        q: deque[int] = deque()
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while q and arr[i] >= arr[q[0]]:
                q.popleft()
            if q:
                ans[i] = q[0] - i
            q.appendleft(i)
        return ans
