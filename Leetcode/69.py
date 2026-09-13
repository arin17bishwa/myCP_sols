class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        ans = 0
        while lo <= hi:
            mid = (lo + hi) >> 1
            k = mid * mid

            if k > x:
                hi = mid - 1
            elif k < x:
                ans = mid
                lo = mid + 1
            else:
                return mid
        return int(ans)


def main():
    obj = Solution()

    n = 4
    n = 8
    n = 1
    # n = 36
    # n = 0
    # n = 2147395599

    ans = obj.mySqrt(n)

    print(ans)


if __name__ == "__main__":
    main()
