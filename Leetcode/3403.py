class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        s = word
        n = len(s)
        if n == 1 or numFriends == 1:
            return s

        return max(s[i: i + n - numFriends + 1] for i in range(n))
