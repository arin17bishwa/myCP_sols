from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans: List[str] = []
        n = len(words)
        for i in range(n):
            curr = words[i]
            for j in range(n):
                if i == j:
                    continue
                if curr in words[j]:
                    ans.append(curr)
                    break
        return ans
