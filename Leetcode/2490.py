class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        for i in range(1, n):
            if words[i - 1][-1] != words[i][0]:
                return False
        return sentence[0] == sentence[-1]
