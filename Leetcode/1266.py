from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        arr = points
        n = len(arr)
        if n < 2:
            return 0
        last = arr[0]
        ans: int = 0
        for i in range(1, n):
            curr = arr[i]
            mn_diff = min(abs(last[0] - curr[0]), abs(last[1] - curr[1]))
            ans += (
                mn_diff + max(abs(last[0] - curr[0]), abs(last[1] - curr[1])) - mn_diff
            )
            last = curr
        return ans


def main():
    obj = Solution()
    arr = [[1, 1], [3, 4], [-1, 0]]
    arr = [[3, 2], [-2, 2]]

    ans = obj.minTimeToVisitAllPoints(arr)

    print(ans)


if __name__ == "__main__":
    main()
