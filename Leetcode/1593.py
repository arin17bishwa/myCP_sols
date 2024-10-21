from typing import Set, List


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        ans = -1
        for bitmap in range(1, 1 << n):
            sub_strings = self.split_string(s, bitmap)
            if len(sub_strings) == len(set(sub_strings)):
                ans = max(ans, len(sub_strings))
        return ans

    @staticmethod
    def split_string(s: str, bitmap: int) -> List[str]:
        n = len(s)
        substrings: List[str] = []
        curr = []
        for i in range(n):
            if bitmap & (1 << i):
                if curr:
                    substrings.append("".join(curr))
                curr = []
            curr.append(s[i])
        if curr:
            substrings.append("".join(curr))
        return substrings
