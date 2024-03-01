class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        zero_cnt = s.count("0")
        one_cnt = n - zero_cnt
        return "1" * (one_cnt - 1) + "0" * zero_cnt + "1"
