class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans: int = numBottles
        empty_bottles = numBottles
        full_bottles = 0
        k = numExchange
        while empty_bottles >= k:
            empty_bottles -= k
            full_bottles += 1
            k += 1
            empty_bottles += 1
            ans += 1
        return ans


def main():
    obj = Solution()

    a, b = 13, 6
    a, b = 10, 3
    a, b = 100, 1
    ans = obj.maxBottlesDrunk(a, b)

    print(ans)


if __name__ == "__main__":
    main()
