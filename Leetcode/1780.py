class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        quotient = n

        while quotient:
            quotient, mod = divmod(quotient, 3)
            if mod == 2:
                return False
        return True
