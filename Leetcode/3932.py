from math import floor, ceil


class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1:
            return r - l + 1

        def is_eligible(b: int):
            return l <= pow(b, k) <= r

        _l, _r = floor(pow(l, 1 / k)), ceil(pow(r, 1 / k))

        return sum(is_eligible(i) for i in range(_l, _r + 1))
