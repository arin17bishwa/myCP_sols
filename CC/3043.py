from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root: dict = {}
        for n in arr1:
            node = root
            for digit in str(n):
                if digit not in node:
                    node[digit] = {}
                node = node[digit]

        return max(dfs(str(n), root) for n in arr2)


def dfs(s: str, trie: dict):
    curr = 0
    node = trie
    for digit in s:
        if digit not in node:
            return curr
        node = node[digit]
        curr += 1
    return curr
