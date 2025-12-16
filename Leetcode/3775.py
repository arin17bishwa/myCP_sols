class Solution:
    def reverseWords(self, s: str) -> str:

        def count_vowels(word: str) -> int:
            vowels = 0
            for ch in word:
                if ch in "aeiou":
                    vowels += 1
            return vowels

        arr = s.split()
        first_vowel_cnt = count_vowels(arr[0])
        n = len(arr)
        for i in range(1, n):
            if count_vowels(arr[i]) == first_vowel_cnt:
                arr[i] = arr[i][::-1]
        return " ".join(arr)
