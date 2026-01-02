from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        comparator = [lambda x, y: x < y, lambda x, y: x > y]
        idx = 0
        inc_flag = False
        for i in range(n - 1):
            if comparator[idx](arr[i], arr[i + 1]):
                inc_flag = True
                continue
            else:
                idx += 1

            if inc_flag and idx == 1 and comparator[idx](arr[i], arr[i + 1]):
                continue
            else:
                return False
        return idx == 1 and inc_flag
