from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        arr = nums
        m = len(arr)

        for i in range(m):
            for j in range(i + 1, min(m, i + 4)):
                if arr[i] == arr[j]:
                    return arr[i]
        return -1
