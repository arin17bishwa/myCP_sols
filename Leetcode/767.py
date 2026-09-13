from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)
        mx = max(freq.values())

        if (n + 1) >> 1 < mx:
            return ""

        ans: list[str] = [""] * n
        it = iter(list(range(0, n, 2)) + list(range(1, n, 2)))

        for k, v in sorted(freq.items(), key=lambda x: -x[1]):
            while v:
                ans[next(it)] = k
                v -= 1

        return "".join(ans)


def main():
    obj = Solution()

    s = "aab"
    s = "aaab"
    s = "baaba"

    ans = obj.reorganizeString(s)

    print(ans)


if __name__ == "__main__":
    main()
