from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n=len(words)
        last=groups[0]
        indices:List[int]=[0]

        for idx in range(1,n):
            if groups[idx]!=groups[indices[-1]]:
                indices.append(idx)
        return [words[i] for i in indices]
