from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        mx = 10**9

        if k == 1:
            return ans

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                arr = []
                for x in range(k):
                    for y in range(k):
                        arr.append(grid[i + x][j + y])
                arr.sort()
                curr = mx

                for idx in range(1, len(arr)):
                    if arr[idx] == arr[idx - 1]:
                        continue
                    curr = min(curr, arr[idx] - arr[idx - 1])
                ans[i][j] = curr if curr != mx else 0

        return ans


def main():
    obj = Solution()

    arr = [[1, -2, 3], [2, 3, 5]]
    k = 2

    ans = obj.minAbsDiff(arr, k)

    print(ans)


if __name__ == "__main__":
    main()
