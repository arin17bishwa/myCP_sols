from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix_sum = [0] + nums
        for i in range(1, n + 1):
            self.prefix_sum[i] += self.prefix_sum[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
