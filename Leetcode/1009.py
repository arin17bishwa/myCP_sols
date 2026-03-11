class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 1
        num = n
        while ans <= num:
            ans <<= 1
        return (ans - 1) ^ num
