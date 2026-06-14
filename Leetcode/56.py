from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = intervals
        n = len(arr)
        arr.sort()

        ans = []
        curr: list[int] = arr[0][:]

        for i in range(1, n):
            if arr[i][0] <= curr[1]:
                curr[1] = max(curr[1], arr[i][1])
            else:
                ans.append(curr[:])
                curr = arr[i][:]

        ans.append(curr)

        return ans
