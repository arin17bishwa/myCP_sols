from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        digits[-1] += 1
        if digits[-1] < 10:
            return digits

        for i in range(n - 1, -1, -1):
            sm = digits[i] + carry
            digits[i] = sm % 10
            carry = sm // 10
        if carry:
            digits[0] = digits[0] % 10
            digits = [1] + digits
        return digits
