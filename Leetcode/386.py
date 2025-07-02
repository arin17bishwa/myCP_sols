from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans: list[int] = []

        def dfs(curr: int):
            nonlocal n, ans
            if curr <= n:
                ans.append(curr)
            else:
                return
            if curr * 10 > n:
                return
            for i in range(10):
                dfs(curr * 10 + i)

        start_number: int = 1
        while len(ans) < n:
            dfs(start_number)
            start_number += 1
        return ans
