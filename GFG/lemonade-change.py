from collections import defaultdict
from math import floor


class Solution:
    def canServe(self, arr: list[int]) -> bool:
        change_available = defaultdict(int)
        for ele in arr:
            change_available[ele] += 1
            to_return = ele - 5
            for denomination in (20, 10, 5):
                mn = min(
                    change_available[denomination], floor(to_return / denomination)
                )
                to_return -= mn * denomination
                change_available[denomination] -= mn
            if to_return:
                return False
        return True
