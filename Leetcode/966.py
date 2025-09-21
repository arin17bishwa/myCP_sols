from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def de_vowel_word(key_word: str) -> str:
            intermediate = list(key_word)
            for idx, ch in enumerate(intermediate):
                if ch in "aeiou":
                    intermediate[idx] = "_"
            return "".join(intermediate)

        exact_matches: set[str] = set(wordlist)
        case_insensitive_matches: dict[str:str] = {}
        vowel_insensitive_matches: dict[str, str] = {}

        for word in wordlist:
            key = word.lower()
            if key not in case_insensitive_matches:
                case_insensitive_matches[key] = word

            key = de_vowel_word(word.lower())
            if key not in vowel_insensitive_matches:
                vowel_insensitive_matches[key] = word

        def find_match(qword: str) -> str:
            nonlocal exact_matches, case_insensitive_matches, vowel_insensitive_matches
            if qword in exact_matches:
                return qword
            if qword.lower() in case_insensitive_matches:
                return case_insensitive_matches[qword.lower()]
            if de_vowel_word(qword.lower()) in vowel_insensitive_matches:
                return vowel_insensitive_matches.get(de_vowel_word(qword.lower()))
            return ""

        return [find_match(q) for q in queries]
