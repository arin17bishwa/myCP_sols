class Solution:
    def maximizeMedian(self, arr: list[int], k: int) -> int:
        n = len(arr)
        arr.sort()
        arr = arr[(n - 1) >> 1 :]
        lo, hi = arr[0], arr[-1] + k
        while lo <= hi:
            mid = (lo + hi) >> 1
            if self.check(arr, k, mid):
                lo = mid + 1
            else:
                hi = mid - 1
        if n & 1:
            return hi
        return (hi + max(hi, arr[1])) >> 1

    @staticmethod
    def check(arr: list[int], k: int, x: int) -> bool:
        balance = k
        for i in arr:
            balance -= max(0, x - i)
            if balance < 0:
                return False
        return True
