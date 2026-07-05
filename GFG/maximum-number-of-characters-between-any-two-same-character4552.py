class Solution:

    def maxCharGap(self, s: str) -> int:
        first_seen: dict[str, int] = {}
        ans: int = -1

        for idx, ch in enumerate(s):
            if ch not in first_seen:
                first_seen[ch] = idx
            else:
                ans = max(ans, idx - first_seen[ch] - 1)

        return ans
