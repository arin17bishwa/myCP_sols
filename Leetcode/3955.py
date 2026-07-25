class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans: list[str] = []

        def func(curr: list[int] = None, curr_cost: int = 0):
            nonlocal n, ans
            if curr is None:
                curr = []

            if curr_cost > k:
                return

            if len(curr) == n:
                ans.append("".join(map(str, curr)))
                return

            for i in range(2):
                if curr and curr[-1] == 1 and i == 1:
                    continue

                new_cost = curr_cost + i * len(curr)

                if new_cost > k:
                    continue

                curr.append(i)
                func(curr, new_cost)
                curr.pop()

            return

        func([], 0)

        return ans
