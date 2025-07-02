from collections import defaultdict


class Solution:
    def substrCount(self, s: str, k: int) -> int:
        n = len(s)
        freq = defaultdict(int)
        curr_distinct_cnt: int = 0
        ans = 0
        for i in range(k):
            if not freq[s[i]]:
                curr_distinct_cnt += 1
            freq[s[i]] += 1
        if curr_distinct_cnt == k - 1:
            ans += 1

        for i in range(k, n):
            freq[s[i - k]] -= 1
            if freq[s[i - k]] == 0:
                curr_distinct_cnt -= 1
            freq[s[i]] += 1
            if freq[s[i]] == 1:
                curr_distinct_cnt += 1
            if curr_distinct_cnt == k - 1:
                ans += 1
        return ans
