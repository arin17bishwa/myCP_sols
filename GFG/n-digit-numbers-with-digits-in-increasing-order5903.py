class Solution:
    def increasingNumbers(self, n: int) -> list[int]:
        if n > 9:
            return []
        if n == 1:
            return list(range(10))

        ans: list[int] = []
        arr: list[int] = []

        def backtrack(curr: list[int]):
            nonlocal ans
            if len(curr) == n:
                ans.append(int("".join(map(str, curr))))
                return

            for nxt_dig in range(curr[-1] + 1, 10):
                curr.append(nxt_dig)
                backtrack(curr)
                curr.pop()
            return

        for first_digit in range(1, 11 - n):
            arr.append(first_digit)
            backtrack(arr)
            arr.pop()
        return ans


def main():
    obj = Solution()

    n = 1

    ans = obj.increasingNumbers(n)

    # print(ans)


if __name__ == "__main__":
    main()
