class Solution:
    def maxSum(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n - 1):
            ans = max(ans, arr[i] + arr[i + 1])
        return ans
