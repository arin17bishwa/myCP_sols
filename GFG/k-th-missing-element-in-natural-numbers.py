class Solution:
    def findKthSmall(self, arr: list[int], k: int) -> int:
        arr.sort()
        ans = k
        for ele in arr:
            if ele <= ans:
                ans += 1
        return ans
