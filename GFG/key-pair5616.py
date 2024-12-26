from typing import List


class Solution:
    def twoSum(self, arr: List[int], target: int):
        arr.sort()
        n = len(arr)
        lo, hi = 0, n - 1

        while lo < hi:
            curr = arr[lo] + arr[hi]
            if curr == target:
                return True
            if curr < target:
                lo += 1
            else:
                hi -= 1
        return False
