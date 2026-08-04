class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        n = len(arr)
        pre: list[int] = [0] * n
        pre[0] = arr[0]

        for i in range(1, n):
            pre[i] = max(arr[i], pre[i - 1] + arr[i])

        curr = ans = sum(arr[:k])

        for i in range(k, n):
            curr += arr[i] - arr[i - k]
            ans = max(ans, curr, curr + pre[i - k])
        return ans


def main():
    obj = Solution()

    arr = [1, -2, 2, -3]
    k = 3

    # arr=[1, 1, 1, 1, 1, 1]
    # k=2

    ans = obj.maxSumWithK(arr, k)

    # print(ans)


if __name__ == "__main__":
    main()
