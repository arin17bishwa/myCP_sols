class Trie:

    def __init__(self):
        self.trie: dict[str, Trie] = dict()
        self.is_end: bool = False

    def insert(self, word: str) -> None:
        curr = self

        for ch in word:
            if ch not in curr.trie:
                curr.trie[ch] = Trie()
            curr = curr.trie[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self

        for ch in word:
            nxt = curr.trie.get(ch)
            if nxt is None:
                return False
            curr = nxt
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self

        for ch in prefix:
            curr = curr.trie.get(ch)
            if curr is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
