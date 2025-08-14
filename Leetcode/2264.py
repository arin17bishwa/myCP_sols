class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = max(
            (
                num[end - 3 : end]
                for end in range(3, n + 1)
                if len(set(num[end - 3 : end])) == 1
            ),
            default="",
        )
        return "".join(ans)
