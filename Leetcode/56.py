from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = intervals
        arr.sort()
        ans = []
        for start, end in arr:
            if ans and ans[-1][1] >= start:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])
        return ans
