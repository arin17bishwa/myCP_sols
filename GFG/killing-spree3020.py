class Solution:
    def maxPeopleDefeated(self, p: int) -> int:
        def sum_of_squares(n: int) -> int:
            return ((n * (n + 1) * ((n << 1) | 1)) // 3) >> 1

        for i in range(1, 10**5):
            if sum_of_squares(i) > p:
                return i - 1
        return 0
