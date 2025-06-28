class Solution:
    def countLessEq(self, a: list[int], b: list[int]):
        b.sort()
        return [self.upper_bound(b, i) + 1 for i in a]

    @staticmethod
    def upper_bound(arr: list[int], target: int) -> int:
        hi, lo = len(arr) - 1, 0
        ans = -1
        while lo <= hi:
            mid = (lo + hi) >> 1
            x = arr[mid]
            if x <= target:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
