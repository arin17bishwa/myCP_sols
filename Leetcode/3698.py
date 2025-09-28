from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        is_inc = [0] * n
        is_dec = [0] * n
        prefix_sum = arr[:]
        is_inc[0] = 1
        is_dec[-1] = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                is_inc[i] = 1
            else:
                break

        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                is_dec[i] = 1
            else:
                break

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]

        ans = 10**18

        for i in range(n - 1):
            if is_inc[i] and is_dec[i + 1]:
                ans = min(ans, abs(prefix_sum[i] - (prefix_sum[-1] - prefix_sum[i])))
        return -1 if ans == 10**18 else ans
