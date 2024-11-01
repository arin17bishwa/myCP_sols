from itertools import groupby


class Solution:
    def makeFancyString(self, s: str) -> str:
        return "".join((ch * min(2, len(tuple(it))) for ch, it in groupby(s)))
