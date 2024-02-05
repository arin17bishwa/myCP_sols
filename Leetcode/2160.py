class Solution:
    def minimumSum(self, num: int) -> int:
        digits = list(str(num))
        digits.sort()
        num1 = "".join((digits[0], digits[2]))
        num2 = "".join((digits[1], digits[3]))
        return int(num1) + int(num2)
