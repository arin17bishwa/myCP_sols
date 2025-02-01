from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        arr = nums
        n = len(arr)
        prev = arr[0]
        for i in range(1, n):
            if prev & 1 == arr[i] & 1:
                return False
            prev = arr[i]
        return True
