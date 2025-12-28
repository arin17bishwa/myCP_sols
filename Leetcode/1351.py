from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        i, j = m - 1, 0
        while i >= 0 and j < n:
            curr = grid[i][j]
            if curr < 0:
                ans += n - j
                i -= 1
            else:
                j += 1
        return ans


def main():
    obj = Solution()

    arr = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    arr = [[3, 2], [1, 0]]

    ans = obj.countNegatives(arr)
    print(ans)


if __name__ == "__main__":
    main()
