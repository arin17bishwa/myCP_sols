from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        ans = 0
        prefix_max = arr[:]
        suffix_max = arr[:]

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i], prefix_max[i - 1])
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i], suffix_max[i + 1])

        for j in range(1, n - 1):
            ans = max(ans, (prefix_max[j - 1] - arr[j]) * suffix_max[j + 1])
        return ans
