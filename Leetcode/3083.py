class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        seen: set[str] = set((s[i + 1] + s[i] for i in range(n - 1)))
        for i in range(n - 1):
            if s[i : i + 2] in seen:
                return True
        return False


def main():
    obj = Solution()

    s = "leetcode"
    s = "abcba"
    s = "abcd"

    ans = obj.isSubstringPresent(s)

    print(ans)


if __name__ == "__main__":
    main()
