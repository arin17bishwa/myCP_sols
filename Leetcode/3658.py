from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return gcd(sum(range(1, (n << 1) | 1, 2)), sum(range(2, (n << 1) | 1, 2)))


def main():
    obj = Solution()

    n = 4

    ans = obj.gcdOfOddEvenSums(n)

    print(ans)


if __name__ == "__main__":
    main()
