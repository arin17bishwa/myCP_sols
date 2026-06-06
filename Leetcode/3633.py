from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        m, n = len(landDuration), len(waterDuration)
        ans = 10**9

        for i in range(m):
            end_land = landStartTime[i] + landDuration[i]
            for j in range(n):
                ans = min(ans, max(end_land, waterStartTime[j]) + waterDuration[j])

        for j in range(n):
            end_water = waterStartTime[j] + waterDuration[j]
            for i in range(m):
                ans = min(ans, max(end_water, landStartTime[i]) + landDuration[i])

        return ans


def main():
    obj = Solution()
    a, b, c, d = [2, 8], [4, 1], [6], [3]
    a, b, c, d = [5], [3], [1], [10]

    ans = obj.earliestFinishTime(a, b, c, d)

    print(ans)


if __name__ == "__main__":
    main()
