from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = intervals
        n = len(arr)
        arr.sort()
        ans = []
        curr = arr[0]
        for idx in range(1, n):
            start, end = arr[idx]
            if start <= curr[1]:
                curr[1] = max(curr[1], end)
            else:
                ans.append(curr[:])
                curr = [start, end]
        ans.append(curr[:])
        return ans
