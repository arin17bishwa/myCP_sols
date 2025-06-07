from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        arr = digits
        n = len(arr)
        candidates: set[int] = set()
        for i in range(n):
            if arr[i] == 0:
                continue
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if arr[k] & 1:
                        continue
                    candidates.add(arr[i] * 100 + arr[j] * 10 + arr[k])
        return sorted(candidates)
