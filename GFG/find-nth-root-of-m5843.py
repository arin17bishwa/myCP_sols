class Solution:
    def nthRoot(self, n: int, m: int) -> int:
        if m == 0:
            return 0
        lo, hi = 1, m
        while lo <= hi:
            mid = (lo + hi) >> 1
            x = pow(mid, n)
            if x == m:
                return mid
            elif x < m:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


def main():
    obj = Solution()
    n, m = 3, 8
    n, m = 3, 9
    n, m = 4, 16
    n, m = 6, 0

    ans = obj.nthRoot(n, m)

    # print(ans)


if __name__ == "__main__":
    main()
