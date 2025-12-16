from collections import Counter


class Solution:
    def findDuplicates(self, arr: list[int]) -> list[int]:
        return [i for i, j in Counter(arr).items() if j != 1]
