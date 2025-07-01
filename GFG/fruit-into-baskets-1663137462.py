from collections import defaultdict


class Solution:
    def totalElements(self, arr: list[int]):
        freq = defaultdict(int)
        unique_cnt = 0
        tail = 0
        n = len(arr)
        ans = 1
        for head in range(n):
            freq[arr[head]] += 1
            if freq[arr[head]] == 1:
                unique_cnt += 1
            while unique_cnt > 2:
                freq[arr[tail]] -= 1
                if freq[arr[tail]] == 0:
                    unique_cnt -= 1
                tail += 1
            ans = max(ans, head - tail + 1)
        return ans
