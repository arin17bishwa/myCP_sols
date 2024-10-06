class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        n1, n2 = len(s1), len(s2)

        traversed = i = x = 0
        while i < n1 and x < n2 and s1[i] == s2[x]:
            i += 1
            x += 1
            traversed += 1
        if traversed == n1:
            return True

        j, y = n1 - 1, n2 - 1
        while j >= i and y >= x and s1[j] == s2[y]:
            j -= 1
            y -= 1
            traversed += 1
        return traversed == min(n1, n2)
