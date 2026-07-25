class Solution:
    def maxArea(self, height: list[int]) -> int:
        arr = height
        n = len(arr)
        j = n - 1
        ans = i = 0

        while i <= j:
            ans = max(ans, min(arr[i], arr[j]) * (j - i - 1))
            if arr[i] <= arr[j]:
                i += 1
            else:
                j -= 1
        return ans
