class Solution:
    def isBinaryPalindrome(self, n: int) -> bool:
        b = bin(n)[2:]
        return b == b[::-1]
