class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 and num2:
            ans += num2 // num1
            num2 %= num1
            num1, num2 = num2 % num1, num1
        return ans
