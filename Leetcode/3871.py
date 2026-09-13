class Solution:
    def countCommas(self, n: int) -> int:
        ans: int = 0
        exp: int = 1
        while pow(10, 3 * exp) <= n:
            ans += (exp - 1) * (pow(10, 3 * exp) - pow(10, 3 * (exp - 1)))
            exp += 1
        exp -= 1
        return ans + exp * (n - pow(10, 3 * exp) + 1)
