from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans: list[str] = []
        for word in words:
            ans.extend(word.split(sep=separator))
        return [i for i in ans if i]
