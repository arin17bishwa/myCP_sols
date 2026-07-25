class Solution:
    def sumAndMultiply(self, n: int) -> int:
        return 0 if n == 0 else sum(map(int, str(n))) * int(str(n).replace("0", ""))
