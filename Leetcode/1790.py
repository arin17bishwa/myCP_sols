class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        mis_matches = []
        for i in range(n):
            if s1[i] != s2[i]:
                mis_matches.append(i)
                if len(mis_matches) > 2:
                    return False
        if len(mis_matches) == 1:
            return False
        return (
            True
            if (
                (not mis_matches)
                or (
                    s1[mis_matches[0]] == s2[mis_matches[1]]
                    and s1[mis_matches[1]] == s2[mis_matches[0]]
                )
            )
            else False
        )
