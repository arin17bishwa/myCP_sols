from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        return min([freq["b"], freq["a"], freq["l"] >> 1, freq["o"] >> 1, freq["n"]])
