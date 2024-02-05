class Solution:
    def alternateDigitSum(self, n: int) -> int:
        mul = 1
        ans = 0
        for _digit in str(n):
            ans += int(_digit) * mul
            mul *= -1
        return ans
