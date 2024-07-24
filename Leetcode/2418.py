from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [
            ele[0]
            for ele in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        ]
