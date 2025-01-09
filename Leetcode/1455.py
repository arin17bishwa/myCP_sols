from typing import List


def word_split(sentence: str):
    n = len(sentence)
    word: List[str] = []

    for ch in sentence:
        if ch == " ":
            yield "".join(word)
            word = []
            continue
        word.append(ch)

    if word:
        yield "".join(word)


def match_prefix(word: str, prefix: str) -> bool:
    n = len(prefix)
    if n > len(word):
        return False
    for i in range(n):
        if prefix[i] != word[i]:
            return False
    return True


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, word in enumerate(word_split(sentence), start=1):
            if match_prefix(word, searchWord):
                return idx
        return -1
