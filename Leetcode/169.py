from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        candidate_freq = 0
        for i in nums:
            if i == candidate:
                candidate_freq += 1
            else:
                candidate_freq -= 1
                if candidate_freq == -1:
                    candidate_freq = 1
                    candidate = i
        return candidate
