class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


def main():
    obj = Solution()

    n = 43261596

    ans = obj.reverseBits(n)

    print(ans)


if __name__ == "__main__":
    main()
