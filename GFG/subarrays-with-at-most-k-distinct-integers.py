from collections import defaultdict


class Solution:
    def countAtMostK(self, arr: list[int], k: int) -> int:
        n = len(arr)
        tail = ans = unique_cnt = 0
        freq = defaultdict(int)
        for head in range(n):
            freq[arr[head]] += 1
            if freq[arr[head]] == 1:
                unique_cnt += 1

            while unique_cnt > k:
                freq[arr[tail]] -= 1
                if freq[arr[tail]] == 0:
                    unique_cnt -= 1
                tail += 1
            ans += head - tail + 1
        return ans
