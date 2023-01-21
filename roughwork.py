from typing import *
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.is_word = False

    def has_node(self, key: str) -> bool:
        return self.nodes.get(key) is not None

    def get_next_node(self, key: str):
        return self.nodes[key]

    def __str__(self):
        return f"({self.nodes},{self.is_word})"


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            curr = curr.get_next_node(ch)
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if not curr.has_node(ch):
                return False
            curr = curr.get_next_node(ch)
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if not curr.has_node(ch):
                return False
            curr = curr.get_next_node(ch)
        return True


from collections import deque


def func(n: int, s: str):
    l1 = deque(list(s))
    freq = [0] * 26

    for i in l1:
        freq[ord(i) - 97] += 1
    l2 = []
    ans = []
    i = 0
    while l1:
        x = l1.popleft()
        _x = ord(x) - 97
        if _x == i:
            ans.append(x)
        else:
            l2.append(x)
        freq[_x] -= 1
        if freq[_x] == 0:
            i += 1
    while l2:
        ans.append(l2.pop())
    return ''.join(ans)


class A:
    def __init__(self, name=''):
        self.name = name

    def __repr__(self):
        return f'{self.name}Layer'


class B(A):
    def __init__(self, size):
        super().__init__('B')
        self.size = size


class C(A):
    def __init__(self, size):
        super().__init__('C')
        self.size = size


if __name__ == '__main__':
    s = 'add'
    print(func(len(s), s))
