class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans: list[str] = []

        def func(curr: list[int] = None, curr_cost: int = 0):
            nonlocal n, ans
            if curr is None:
                curr = []

            if curr_cost>k:
                return

            if len(curr) == n:
                ans.append("".join(map(str, curr)))
                return

            if curr and curr[-1] == 1:
                curr.append(0)
                func(curr, curr_cost)
                curr.pop()
            else:
                for i in range(2):
                    curr.append(i)
                    func(curr, curr_cost + i * (len(curr) - 1))
                    curr.pop()

            return

        func([], 0)

        return ans
