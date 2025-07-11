from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.tree = defaultdict(TrieNode)
        self.ends: bool = False


class Trie:

    def __init__(self):
        self.tree: dict[str, TrieNode] = defaultdict(TrieNode)

    def insert(self, word: str) -> None:
        curr: TrieNode | Trie = self
        for ch in word:
            curr = curr.tree[ch]
        curr.ends = True

    def search(self, word: str) -> bool:
        curr: Trie | TrieNode = self
        for ch in word:
            if ch not in curr.tree:
                return False
            curr = curr.tree[ch]
        return curr.ends

    def startsWith(self, prefix: str) -> bool:
        curr: Trie | TrieNode = self
        for ch in prefix:
            if ch not in curr.tree:
                return False
            curr = curr.tree[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
