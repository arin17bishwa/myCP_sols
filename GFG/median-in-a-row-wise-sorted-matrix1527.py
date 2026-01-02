class Solution:
    def median(self, mat: list[list[int]]) -> int:
        mn = min(row[0] for row in mat)
        mx = max(row[-1] for row in mat)

        n = len(mat) * len(mat[0])
        lo, hi = mn, mx
        ans = lo
        threshold = (n + 1) >> 1

        while lo <= hi:
            mid = (lo + hi) >> 1
            cnt = sum(self._le(row, mid) for row in mat)

            if cnt >= threshold:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

    @staticmethod
    def _le(row: list[int], k: int) -> int:
        ans = -1
        lo, hi = 0, len(row) - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if row[mid] <= k:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans + 1
