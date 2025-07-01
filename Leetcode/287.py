from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = nums
        for i in range(len(arr)):
            temp = arr[i]
            if arr[abs(temp)] < 0:
                return abs(temp)
            arr[abs(temp)] *= -1
        return -1
