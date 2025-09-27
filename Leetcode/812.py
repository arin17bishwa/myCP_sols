from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def herons_area(p1: list[int], p2: list[int], p3: list[int]) -> float:
            a, b, c = length(p1, p2), length(p2, p3), length(p1, p3)
            s = (a + b + c) / 2
            return pow(
                max(0.0, s * round(s - a, 7) * round(s - b, 7) * round(s - c, 7)), 0.5
            )

        def length(p1: list[int], p2: list[int]) -> float:
            return pow((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2, 0.5)

        ans = 0
        n = len(points)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    ans = max(ans, herons_area(points[i], points[j], points[k]))
        return ans


def main():
    obj = Solution()
    arr = [
        [-35, 19],
        [40, 19],
        [27, -20],
        [35, -3],
        [44, 20],
        [22, -21],
        [35, 33],
        [-19, 42],
        [11, 47],
        [11, 37],
    ]

    ans = obj.largestTriangleArea(arr)

    print(ans)


if __name__ == "__main__":
    main()
