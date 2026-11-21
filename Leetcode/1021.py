class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans: list[str] = []
        curr = 0

        for idx, ele in enumerate(s):
            if ele == "(":
                curr += 1
                if curr > 1:
                    ans.append(ele)
            else:
                curr -= 1
                if curr > 0:
                    ans.append(ele)
        return "".join(ans)
