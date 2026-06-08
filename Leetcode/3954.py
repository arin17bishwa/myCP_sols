class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        return sum(i if n & i == 0 else 0 for i in range(max(0, n - k), n + k + 1))
