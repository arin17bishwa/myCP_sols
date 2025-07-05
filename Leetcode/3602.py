import string


class Solution:
    def concatHex36(self, n: int) -> str:
        return self.int_to_base(n**2, 16) + self.int_to_base(n**3, 36)

    @staticmethod
    def int_to_base(n: int, base: int) -> str:
        if n == 0:
            return "0"
        chars = list(string.digits + string.ascii_uppercase)
        ans = []

        while n:
            ans.append(chars[n % base])
            n //= base
        return "".join(ans[::-1])
