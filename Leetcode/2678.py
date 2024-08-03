from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(i[11:13] > "60" for i in details)
