class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)

        if n == 1 or numFriends == 1:
            return word

        if n == numFriends:
            return max(word)
        return max(word[i : i + (n - numFriends + 1)] for i in range(n))
