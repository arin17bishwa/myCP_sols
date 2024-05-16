class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        t_idx: dict[str:int] = {ele: idx for idx, ele in enumerate(t)}
        return sum((abs(idx - t_idx[ele]) for idx, ele in enumerate(s)))
