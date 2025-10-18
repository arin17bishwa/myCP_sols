from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)

        if any(v > (1 + n) // 2 for v in freq.values()):
            return ""

        chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        ans: list[str] = [""] * n
        curr_idx = 0
        for ch in chars:
            for _ in range(freq[ch]):
                if curr_idx >= n:
                    curr_idx = 1
                ans[curr_idx] = ch
                curr_idx += 2

        return "".join(ans)
