from typing import List


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost: List[int] = [abs(ord(i) - ord(j)) for i, j in zip(s, t)]
        n = len(cost)
        tail = 0
        curr_cost = 0
        ans = 0
        for head in range(n):
            curr_cost += cost[head]
            while curr_cost > maxCost and tail <= head:
                curr_cost -= cost[tail]
                tail += 1
            if curr_cost <= maxCost:
                ans = max(ans, head - tail + 1)
        return ans
