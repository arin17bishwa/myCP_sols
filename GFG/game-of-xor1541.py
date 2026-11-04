class Solution:
    def subarrayXor(self, arr: list[int]) -> int:
        ans = 0
        n = len(arr)

        for idx, ele in enumerate(arr):
            if ((idx + 1) * (n - idx)) & 1:
                ans ^= ele
        return ans
