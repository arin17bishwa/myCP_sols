from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        return min(self.min_groupings(nums, 0), self.min_groupings(nums, 1))

    @staticmethod
    def min_groupings(arr: List[int], key: int):
        n = len(arr)
        total_keys = arr.count(key)
        window_size = total_keys
        current_keys = arr[:total_keys].count(key)
        ans = total_keys - current_keys
        for head in range(window_size, n):
            current_keys += arr[head] == key
            current_keys -= arr[head - window_size] == key
            ans = min(ans, total_keys - current_keys)
        return ans
