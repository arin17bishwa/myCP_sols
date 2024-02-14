from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for i in nums:
            if i >= 0:
                positive.append(i)
            else:
                negative.append(i)
        ans = []
        for i, j in zip(positive, negative):
            ans.extend([i, j])
        return ans
