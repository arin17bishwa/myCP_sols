from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        arr = nums
        n = len(arr)

        valid_ranges: List[List[int]] = []

        start = 0
        last_parity = -1
        for i in range(n):
            curr_parity: int = arr[i] % 2
            if curr_parity == last_parity:
                valid_ranges.append([start, i - 1])
                start = i
            last_parity = curr_parity

        if not valid_ranges or (valid_ranges and valid_ranges[-1][-1] != n - 1):
            valid_ranges.append([start, n - 1])

        starting_points: List[int] = [i[0] for i in valid_ranges]

        ans: List[bool] = []

        for q_start, q_end in queries:
            idx = bisect_right(starting_points, q_start) - 1
            ans.append(valid_ranges[idx][1] >= q_end)

        return ans
