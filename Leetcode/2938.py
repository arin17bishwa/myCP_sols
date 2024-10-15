class Solution:
    def minimumSteps(self, s: str) -> int:
        ans: int = 0
        req_idx: int = 0
        for curr_idx, ele in enumerate(s):
            if ele == "0":
                ans += abs(curr_idx - req_idx)
                req_idx += 1
        return ans
