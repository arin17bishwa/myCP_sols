class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k & 1 == 0 or k % 5 == 0:
            return -1
        prev_rem = 1
        seen: set[int] = set()
        ans = 1
        while prev_rem not in seen:
            ans += 1
            seen.add(prev_rem)
            new_rem = (((prev_rem * 10) % k) + 1) % k
            if new_rem == 0:
                return ans
            prev_rem = new_rem
        return -1


def main():
    obj = Solution()

    k = 3
    k = 7
    # k = 2

    ans = obj.minAllOneMultiple(k)

    print(ans)


if __name__ == "__main__":
    main()
