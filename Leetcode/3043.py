from typing import List


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, s: str):
        trie = self.trie
        for ch in s:
            if ch not in trie:
                trie[ch] = {}
            trie = trie[ch]

    def longest_prefix(self, s: str) -> int:
        trie = self.trie
        length = 0
        for ch in s:
            if ch not in trie:
                return length
            trie = trie[ch]
            length += 1
        return length


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        trie = Trie()
        for word in arr1:
            trie.insert(str(word))
        return max(trie.longest_prefix(str(s)) for s in arr2)
