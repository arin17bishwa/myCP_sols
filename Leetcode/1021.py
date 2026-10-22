class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        arr: list[int] = [0] * n
        curr = 0

        for idx, ele in enumerate(s):
            if ele == "(":
                curr += 1
            else:
                curr -= 1
            arr[idx] = curr
        return "".join(
            (
                s[idx]
                if ((ele > 1 and s[idx] == "(") or (ele > 0 and s[idx] == ")"))
                else ""
            )
            for idx, ele in enumerate(arr)
        )


def main():
    obj = Solution()

    s = "(()())(())"
    s = "(()())(())(()(()))"
    s = "()()"

    ans = obj.removeOuterParentheses(s)

    print(ans)


if __name__ == "__main__":
    main()
