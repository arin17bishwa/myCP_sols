class Solution:
    def reverseDegree(self, s: str) -> int:
        ans: int = 0

        for idx, ch in enumerate(s):
            ans += (123 - ord(ch)) * (idx + 1)
        return ans
