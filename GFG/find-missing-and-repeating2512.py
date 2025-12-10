from collections import Counter


class Solution:
    def findTwoElement(self, arr: list[int]) -> list[int]:
        n = len(arr)
        freq = Counter(arr)
        ans = [-1, -1]
        for i in range(1, 1 + n):
            if freq[i] == 2:
                ans[0] = i
            elif freq[i] == 0:
                ans[1] = i
        return ans
