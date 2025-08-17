class Solution:
    def maximum69Number(self, num: int) -> int:
        for i in range(5, -1, -1):
            if (num // pow(10, i)) % 10 == 6:
                num += 3 * (pow(10, i))
                break
        return num


def main():
    obj = Solution()
    n = 9669
    ans = obj.maximum69Number(n)

    print(ans)


if __name__ == "__main__":
    main()
