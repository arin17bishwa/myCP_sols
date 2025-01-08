from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children: defaultdict = defaultdict(lambda: TrieNode())
        self.count = 0


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, s: str):
        curr = self.trie

        for ch1, ch2 in zip(s, reversed(s)):
            curr: TrieNode = curr.children[(ch1, ch2)]
            curr.count += 1

    def count(self, s: str) -> int:
        curr = self.trie

        for ch1, ch2 in zip(s, reversed(s)):
            if (ch1, ch2) not in curr.children:
                return 0
            curr: TrieNode = curr.children[(ch1, ch2)]

        return curr.count


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()

        ans = 0
        for word in reversed(words):
            ans += trie.count(word)
            trie.insert(word)

        return ans
