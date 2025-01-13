class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        return sum(
            (str(num)[i: i + k] != "0" * k) and (num % int(str(num)[i: i + k]) == 0)
            for i in range(len(str(num)) - k + 1)
        )
