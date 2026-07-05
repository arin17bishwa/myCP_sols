from collections import defaultdict


class Solution:

    def maxCharGap(self, s: str) -> int:
        first_seen: defaultdict[str, int] = defaultdict(lambda: 1 << 31)
        ans = -1

        for idx, ch in enumerate(s):
            if ch not in first_seen:
                first_seen[ch] = idx
            else:
                ans = max(ans, idx - first_seen[ch] - 1)

        return ans
