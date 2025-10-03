from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq: defaultdict[str, int] = defaultdict(int)
        n = len(s)
        tail: int = 0
        ans = 0
        for head, ch in enumerate(s):
            freq[ch] += 1
            while freq[ch] > 1:
                freq[s[tail]] -= 1
                tail += 1
            ans = max(ans, head - tail + 1)
        return ans
