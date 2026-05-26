from collections import Counter


class Solution:
    def isProduct(self, arr: list[int], target: int) -> bool:
        freq = Counter(arr)

        for k, v in freq.items():
            if k == 0:
                continue
            if target % k == 0:
                dividend = target // k
                if dividend == k and v >= 2:
                    return True
                elif dividend != k and freq[dividend] >= 1:
                    return True
        return False
