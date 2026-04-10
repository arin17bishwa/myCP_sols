class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)

        arr1 = [[0] * 26 for _ in range(2)]
        arr2 = [[0] * 26 for _ in range(2)]

        for idx, ch in enumerate(s1):
            arr1[(idx & 1) != 0][ord(ch) - 97] += 1

        for idx, ch in enumerate(s2):
            arr2[(idx & 1) != 0][ord(ch) - 97] += 1

        return arr1 == arr2
