from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr = nums

        candidate = arr[0]
        freq = 0

        for i in arr:
            if i == candidate:
                freq += 1
            else:
                freq -= 1
                if freq < 0:
                    candidate = i
                    freq = 1
        return candidate
