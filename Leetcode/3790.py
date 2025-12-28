class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k & 1 == 0 or k % 5 == 0:
            return -1
        prev_rem = 1
        ans = 1
        seen: set[int] = set()

        while prev_rem not in seen:
            ans += 1
            seen.add(prev_rem)
            new_rem = (((prev_rem * 10) % k) + 1) % k
            if new_rem == 0:
                return ans
            prev_rem = new_rem
        return -1
