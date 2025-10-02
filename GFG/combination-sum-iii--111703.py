class Solution:
    def combinationSum(self, n: int, k: int) -> list[list[int]]:

        ans: list[list[int]] = []

        def func(curr_sum: int, curr: list[int]):
            nonlocal n, ans
            if len(curr) == k and curr_sum == n:
                ans.append(curr[:])
            if curr_sum > n or len(curr) >= k:
                return
            for i in range(curr[-1] + 1 if curr else 1, 10):
                curr.append(i)
                curr_sum += i
                func(curr_sum, curr)
                curr.pop()
                curr_sum -= i

        func(0, [])
        return ans
