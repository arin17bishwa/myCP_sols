from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = nums
        n = len(arr)

        for ele in arr:
            if arr[abs(ele) - 1] > 0:
                arr[abs(ele) - 1] *= -1
        return [i + 1 for i in range(n) if arr[i] > 0]
