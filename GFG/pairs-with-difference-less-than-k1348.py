class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        arr.sort()
        n = len(arr)

        ans = j = 0

        for i in range(n):
            while j < n and arr[j] - arr[i] < k:
                j += 1
            ans += j - i - 1

        return ans


def main():
    obj = Solution()

    arr = [1, 10, 4, 2]
    k = 3

    arr = [2, 3, 4]
    k = 5

    ans = obj.countPairs(arr, k)

    # print(ans)


if __name__ == "__main__":
    main()
