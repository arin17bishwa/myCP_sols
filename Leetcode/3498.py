class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(idx * (123 - ord(ch)) for idx, ch in enumerate(s, start=1))
