class Solution:
    def subarrayXor(self, arr: list[int]) -> int:
        ans = 0
        n = len(arr)

        for i in range(n):
            if ((i + 1) * (n - i)) & 1:
                ans ^= arr[i]
        return ans
