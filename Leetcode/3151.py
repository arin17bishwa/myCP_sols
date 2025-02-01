from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        arr = nums
        n = len(arr)
        for i in range(1, n):
            if (arr[i - 1] ^ arr[i]) & 1 == 0:
                return False
        return True
