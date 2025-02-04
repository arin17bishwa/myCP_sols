from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        target_freq = n >> 1
        candidate = ""
        curr = 0
        for ele in arr:
            if ele == candidate:
                curr += 1
            else:
                curr -= 1
            if curr < 0:
                candidate = ele
                curr = 1
        return candidate
