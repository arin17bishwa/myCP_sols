class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        ans = 0
        min_need = min(need1, need2)
        ans += min_need * min(costBoth, cost1 + cost2)
        need1 -= min_need
        need2 -= min_need
        if need1 > 0:
            ans += need1 * min(costBoth, cost1)
        if need2 > 0:
            ans += need2 * min(costBoth, cost2)
        return ans
