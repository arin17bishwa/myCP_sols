class Solution:
    def subsequenceSum(self, s: str) -> int:
        n = len(s)
        ans: int = 0
        mod = 10**9 + 7
        for ch in s:
            ans = (ans + (int(ch) * pow(2, n - 1, mod))) % mod
        return ans
