class Solution:
    def maxLength(self, arr: list[int]) -> int:
        n = len(arr)
        for i in range(1, n):
            arr[i] += arr[i - 1]
        first_occ: dict[int, int] = {0: -1}
        ans: int = 0
        for idx, ele in enumerate(arr):
            if ele not in first_occ:
                first_occ[ele] = idx
            else:
                ans = max(ans, idx - first_occ[ele])
        return ans
