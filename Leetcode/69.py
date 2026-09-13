class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x + 1
        ans = lo
        e = 1e-6
        while (hi - lo) >= e:
            mid = (lo + hi) / 2
            # print(lo, hi, mid)
            k = mid * mid
            if (k - x) >= e:
                hi = mid
                ans = mid
            else:
                lo = mid
        return int(ans)


def main():
    obj = Solution()

    n = 4
    n = 8
    n = 1
    n = 36
    n = 0
    n = 2147395599

    ans = obj.mySqrt(n)

    print(ans)


if __name__ == "__main__":
    main()
