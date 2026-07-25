class Trie:
    def __init__(self):
        self.trie: dict[str, Trie] = {}
        self.is_end: bool = False

    def insert(self, word: str):
        curr = self

        for ch in word:
            if ch not in curr.trie:
                curr.trie[ch] = Trie()
            curr = curr.trie[ch]
        curr.is_end = True

    def dfs(self, s: str, idx: int = 0) -> bool:
        curr = self
        n = len(s)

        for i in range(idx, n):
            if s[i] == ".":
                if not curr.trie:
                    return False
                return any(node.dfs(s, i + 1) for node in curr.trie.values())
            else:
                nxt = curr.trie.get(s[i])
                if not nxt:
                    return False
                curr = nxt
        return curr and curr.is_end


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.dfs(word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
