from collections import defaultdict


class Solution:
    def subarrayXor(self, arr: list[int], k: int) -> int:
        n = len(arr)

        for i in range(1, n):
            arr[i] ^= arr[i - 1]

        seen: defaultdict[int, int] = defaultdict(int)
        seen[0] += 1
        ans = 0

        for idx, ele in enumerate(arr):
            ans += seen[ele ^ k]
            seen[ele] += 1
        return ans
