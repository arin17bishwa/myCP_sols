from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr = intervals
        n = len(arr)
        arr.sort()
        ans: int = 0
        prev_end: int = arr[0][1]

        for i in range(1, n):
            if arr[i][0] < prev_end:
                ans += 1
                prev_end = min(prev_end, arr[i][1])
            else:
                prev_end = arr[i][1]

        return ans
