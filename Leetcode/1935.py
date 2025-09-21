class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum(
            len(set(brokenLetters).intersection(set(word))) == 0
            for word in text.split()
        )
