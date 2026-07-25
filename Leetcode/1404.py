class Solution:
    def numSteps(self, s: str) -> int:
        n: int = len(s)
        ops = carry = 0

        for i in range(n - 1, 0, -1):

            if ((s[i] == "1") + carry) & 1:
                ops += 2
                carry = 1
            else:
                ops += 1

        return ops + carry
