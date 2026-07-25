from collections import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(int(i) * j for i, j in Counter(str(n)).items())
