class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x // r) >> 1
        return r


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
