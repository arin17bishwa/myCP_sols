import string


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        return sum((i in s) and (i.upper() in s) for i in string.ascii_lowercase)
