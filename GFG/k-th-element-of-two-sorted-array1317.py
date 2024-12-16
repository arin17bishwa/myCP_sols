from typing import List


class Solution:

    def kthElement(self, a, b, k: int):
        arr1: List[int] = a
        arr2: List[int] = b
        m, n = len(arr1), len(arr2)
        i = j = 0
        if k == 1:
            return min(arr1[0], arr2[0])
        while i < m and j < n:
            x, y = arr1[i], arr2[j]
            if i + j + 1 == k:
                return min(x, y)
            if x < y:
                i += 1
            else:
                j += 1

        while i < m:
            x = arr1[i]
            if i + j + 1 == k:
                return x
            i += 1

        while j < n:
            y = arr2[j]
            if i + j + 1 == k:
                return y
            j += 1
