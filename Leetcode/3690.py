from collections import deque
from typing import List


class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        start, target = tuple(nums1), tuple(nums2)
        n = len(nums1)

        if start == target:
            return 0

        seen, q = {start}, deque([(start, 0)])

        while q:
            arr, steps = q.popleft()
            for left in range(n):
                for right in range(left, n):
                    sub, rem = arr[left : right + 1], arr[:left] + arr[right + 1 :]
                    for k in range(len(rem) + 1):
                        nxt = rem[:k] + sub + rem[k:]
                        if nxt == target:
                            return steps + 1
                        if nxt not in seen:
                            seen.add(nxt)
                            q.append((nxt, steps + 1))
        return -1
