class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n < 3:
            return True
        while n > 1:
            if (n & 1) ^ ((n & 2) >> 1) == 0:
                return False
            n >>= 1
        return True


def main():
    obj = Solution()

    n = 5
    n = 7
    n = 11

    ans = obj.hasAlternatingBits(n)

    print(ans)


if __name__ == "__main__":
    main()
