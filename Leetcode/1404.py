class Solution:
    def numSteps(self, s: str) -> int:
        ops: int = 0
        n: int = len(s)
        carry: int = 0
        for i in range(n - 1, 0, -1):

            if ((s[i] == "1") + carry) & 1:
                ops += 2
                carry = 1
            else:
                ops += 1

        return ops + carry


def main():
    obj = Solution()

    s = "1101"
    s = "10"
    s = "1"

    ans = obj.numSteps(s)

    print(ans)


if __name__ == "__main__":
    main()
