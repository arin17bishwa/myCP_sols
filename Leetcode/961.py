from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        arr = nums
        m = len(arr)

        for i in range(m):
            if arr[i] in arr[i + 1 : i + 4]:
                return arr[i]
        return -1
