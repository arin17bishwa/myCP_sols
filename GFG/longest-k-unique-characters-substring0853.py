from collections import defaultdict


class Solution:
    def longestKSubstr(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        current_distinct_cnt = tail = 0
        ans: int = -1
        for head in range(len(s)):
            freq[s[head]] += 1
            if freq[s[head]] == 1:
                current_distinct_cnt += 1
            while current_distinct_cnt > k:
                freq[s[tail]] -= 1
                if freq[s[tail]] == 0:
                    current_distinct_cnt -= 1
                tail += 1
            if current_distinct_cnt == k:
                ans = max(ans, head - tail + 1)
        return ans
