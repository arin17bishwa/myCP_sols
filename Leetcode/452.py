from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arr = points
        arr.sort()
        curr_min_end = arr[0][-1]
        curr_cnt = 1
        for start, end in arr:
            if start <= curr_min_end:
                curr_min_end = min(curr_min_end, end)
            else:
                curr_min_end = end
                curr_cnt += 1
        return curr_cnt
