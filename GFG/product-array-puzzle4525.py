from typing import List


class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        prefix = arr[:]
        suffix = arr[:]
        n = len(arr)
        for i in range(1, n):
            prefix[i] *= prefix[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] *= suffix[i + 1]

        return (
                [suffix[1]]
                + [prefix[i - 1] * suffix[i + 1] for i in range(1, n - 1)]
                + [prefix[-2]]
        )
