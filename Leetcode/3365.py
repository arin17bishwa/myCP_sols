from collections import Counter


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        segment_len = n // k
        t_freq: Counter[str] = Counter()
        s_freq: Counter[str] = Counter()
        for i in range(0, n, segment_len):
            s_freq[s[i : i + segment_len]] += 1
            t_freq[t[i : i + segment_len]] += 1

        return s_freq == t_freq
