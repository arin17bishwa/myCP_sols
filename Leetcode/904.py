from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        arr = fruits
        n = len(arr)
        start = ans = 0
        seen = defaultdict(int)
        for end in range(n):
            x = arr[end]
            if x not in seen:
                ans = max(ans, sum(seen.values()))
                while len(seen) > 1 and start < end:
                    seen[arr[start]] -= 1
                    if seen[arr[start]] == 0:
                        seen.pop(arr[start])
                    start += 1
            seen[x] += 1
        return max(ans, sum(seen.values()))
