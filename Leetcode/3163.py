from itertools import groupby


class Solution:
    def compressedString(self, word: str) -> str:
        return "".join(
            (f"9{k}" * (v // 9) + f"{v%9}{k}" * (v % 9 != 0))
            for k, v in ((ch, len(tuple(items))) for ch, items in groupby(word))
        )
