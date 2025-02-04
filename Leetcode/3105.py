from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        def longest_increasing_length(arr: List[int]):
            ans = curr = 1
            n = len(arr)
            for i in range(1, n):
                if arr[i - 1] < arr[i]:
                    curr += 1
                    ans = max(ans, curr)
                else:
                    curr = 1
            return ans

        return max(
            longest_increasing_length(nums), longest_increasing_length(nums[::-1])
        )
