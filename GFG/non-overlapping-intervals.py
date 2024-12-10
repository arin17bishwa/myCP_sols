from typing import List


class Solution:
    def minRemoval(self, intervals: List[List[int]]):
        arr = intervals
        arr.sort(key=lambda x: x[1])
        prev_end: int = -1
        ans: int = 0

        for start, end in intervals:
            if start < prev_end:
                ans += 1
            else:
                prev_end = end
        return ans
