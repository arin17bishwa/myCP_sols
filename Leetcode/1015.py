class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k & 1 == 0:
            return -1
        seen: set[int] = set()
        curr = 1
        for length in range(1, k + 1):
            mod = curr % k
            if mod in seen:
                return -1
            if mod == 0:
                return length
            seen.add(mod)
            curr = mod * 10 + 1
        return -1


def main():
    obj = Solution()
    k = 4

    ans = obj.smallestRepunitDivByK(k)

    print(ans)


if __name__ == "__main__":
    main()
