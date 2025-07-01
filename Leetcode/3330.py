from collections import defaultdict


class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        ans = 0
        last_cnt = 0
        for i in range(1, n):
            if word[i] == word[i - 1]:
                last_cnt += 1
            else:
                ans += last_cnt
                last_cnt = 0
        return ans + last_cnt + 1
