import sys

sys.set_int_max_str_digits(10**5 + 1)


class Solution:
    def divby13(self, s: str) -> bool:
        return int(s) % 13 == 0
