from collections import Counter


class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        arr = nums
        freq = Counter(arr)

        ans: list[int] = []
        for key in sorted(freq.keys()):
            ans.extend([key] * min(freq[key], k))

        return ans
