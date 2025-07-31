from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        def k_sum(
            start: int, remaining_target: int, remaining_k: int
        ) -> list[list[int]]:
            nonlocal n, nums
            ans = []
            if start == n:
                return []

            if remaining_k == 2:
                return two_sum(start, remaining_target)

            for i in range(start, n):
                if i == start or nums[i] != nums[i - 1]:
                    for sub_ans in k_sum(
                        i + 1, remaining_target - nums[i], remaining_k - 1
                    ):
                        ans.append([nums[i]] + sub_ans)
            return ans

        def two_sum(start: int, remaining_target: int) -> list[list[int]]:
            nonlocal n, nums
            ans = []
            lo, hi = start, n - 1
            while lo < hi:
                curr = nums[lo] + nums[hi]
                if curr < remaining_target or (lo > start and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr > remaining_target or (
                    hi < n - 1 and nums[hi] == nums[hi + 1]
                ):
                    hi -= 1
                else:
                    ans.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return ans

        return k_sum(0, target, 4)
