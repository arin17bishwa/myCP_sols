from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = candidate2 = -1
        cnt1 = cnt2 = 0

        for i in nums:
            if cnt1 == 0 and i != candidate2:
                cnt1 = 1
                candidate1 = i
            elif cnt2 == 0 and i != candidate1:
                cnt2 = 1
                candidate2 = i
            elif i == candidate1:
                cnt1 += 1
            elif i == candidate2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        ans = []

        for candidate in {candidate1, candidate2}:
            if nums.count(candidate) > (len(nums) // 3):
                ans.append(candidate)
        return ans
