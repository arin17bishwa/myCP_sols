from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        return [self.find_sum(nums[i : i + k], x) for i in range(len(nums) - k + 1)]

    @staticmethod
    def find_sum(arr: list[int], x: int) -> int:
        freq = Counter(arr)
        return sum(
            [
                i[0] * i[1]
                for i in sorted(freq.items(), key=lambda y: (y[1], y[0]), reverse=True)
            ][:x]
        )


def main():
    obj = Solution()

    arr = [1, 1, 2, 2, 3, 4, 2, 3]
    k, x = 6, 2

    ans = obj.findXSum(arr, k, x)

    print(ans)


if __name__ == "__main__":
    main()
