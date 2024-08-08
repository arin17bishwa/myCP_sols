from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = nums
        mod = 10**9 + 7
        prefix_sum = [0] + arr[:]
        for i in range(1, n + 1):
            prefix_sum[i] += prefix_sum[i - 1]
        subarray_sums: List[int] = []
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                subarray_sums.append(prefix_sum[j] - prefix_sum[i - 1])
        subarray_sums.sort()
        ans = 0
        for i in range(left - 1, right):
            ans = (ans + subarray_sums[i]) % mod
        return ans
