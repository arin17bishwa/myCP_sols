from collections import deque


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        arr = nums
        n = len(arr)
        mx = arr[0]
        d: deque[tuple[int, int]] = deque([(n - 1, arr[-1])])

        for i in range(n - 2, -1, -1):
            if arr[i] < d[0][-1]:
                d.appendleft((i, arr[i]))

        for i in range(n):
            mx = max(mx, arr[i])
            if i > d[0][0]:
                d.popleft()
            if mx - d[0][1] <= k:
                return i
        return -1
