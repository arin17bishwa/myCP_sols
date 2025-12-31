from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        int_max = (1 << 32) - 1
        ans = int_max

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if arr[i] < arr[j] and arr[j] > arr[k]:
                        ans = min(ans, arr[i] + arr[j] + arr[k])
        return ans if ans != int_max else -1
