class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31):
            ans |= n & 1
            n >>= 1
            ans <<= 1
        return ans


def main():
    obj = Solution()

    n = 43261596

    ans = obj.reverseBits(n)

    print(ans)


if __name__ == "__main__":
    main()
