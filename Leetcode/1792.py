import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def calculate_gain(p: int, t: int) -> float:
            return ((p + 1) / (t + 1)) - (p / t)

        arr = classes
        arr = [[-calculate_gain(*i)] + i for i in arr]
        heapq.heapify(arr)

        while extraStudents:
            _, pass_, total = heapq.heappop(arr)
            heapq.heappush(
                arr, [-calculate_gain(pass_ + 1, total + 1), pass_ + 1, total + 1]
            )
            extraStudents -= 1

        return sum(i[1] / i[2] for i in arr) / len(arr)


def main():
    obj = Solution()

    arr = [[1, 2], [3, 5], [2, 2]]
    n = 2

    arr = [[2, 4], [3, 9], [4, 5], [2, 10]]
    n = 4
    arr=[[583,868],[783,822],[65,262],[121,508],[461,780],[484,668]]


    ans = obj.maxAverageRatio(arr, n)

    print(ans)


if __name__ == "__main__":
    main()
