class Solution:
    def maxFruits(self, arr: list[int], m: int) -> int:
        n = len(arr)
        curr = sum(arr[:m])
        ans = curr
        for i in range(m, n + m):
            curr = curr - arr[((i - m) % n)] + arr[i % n]
            ans = max(ans, curr)
        return ans


def main():
    obj = Solution()

    arr = [2, 1, 3, 5, 0, 1, 4]
    m = 3

    arr = [1, 6, 2, 5, 3, 4]
    m = 2

    arr = [7, 2, 1, 3, 4]
    m = 2

    ans = obj.maxFruits(arr, m)

    # print(ans)


if __name__ == "__main__":
    main()
