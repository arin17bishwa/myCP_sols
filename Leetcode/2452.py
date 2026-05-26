from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans: list[str] = []

        def is_valid_edit_dist(s1: str, s2: str) -> bool:
            distance = 0
            for i, j in zip(s1, s2):
                if i != j:
                    distance += 1
                    if distance > 2:
                        return False
            return True

        for query in queries:
            for word in dictionary:
                if is_valid_edit_dist(query, word):
                    ans.append(query)
                    break

        return ans
