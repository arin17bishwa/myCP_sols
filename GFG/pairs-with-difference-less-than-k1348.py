class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        arr.sort()
        n = len(arr)

        def search(x: int) -> int:
            nonlocal arr, n
            lo, hi = 0, n - 1
            fin = 0

            while lo <= hi:
                mid = (lo + hi) >> 1
                if arr[mid] < x:
                    lo = mid + 1
                    fin = mid
                else:
                    hi = mid - 1
            return fin

        ans = 0
        for i in range(n):
            ans += max(0, search(arr[i] + k) - i)

        return ans
