class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_cnt = 5
        prime_cnt = 4
        ans = 1
        mod = 10**9 + 7
        for i in range(n):
            if not i & 1:
                ans *= even_cnt
            else:
                ans *= prime_cnt
            ans %= mod
        return ans
