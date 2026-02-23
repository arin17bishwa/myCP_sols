class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        curr = 0
        for i in range(k):
            curr = (curr << 1) | (1 if s[i] == "1" else 0)
        seen = {curr}
        for i in range(k, n):
            curr = (curr << 1) | (1 if s[i] == "1" else 0)
            curr &= (1 << k) - 1
            seen.add(curr)
        return len(seen) == (1 << k)


def main():
    obj = Solution()

    s = "00110110"
    k = 2

    s = "0110"
    k = 2

    ans = obj.hasAllCodes(s, k)

    print(ans)


if __name__ == "__main__":
    main()
