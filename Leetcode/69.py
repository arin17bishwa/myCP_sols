class Solution:
    def mySqrt(self, x: int) -> int:
        def func(n: int) -> int:
            if n < 2:
                return n
            lower_bound = func(n >> 2) << 1
            upper_bound = lower_bound + 1
            return lower_bound if upper_bound * upper_bound > n else upper_bound

        return func(x)


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
