class Solution:

    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        if n & 1:
            return False

        # check closing brackets
        opening_bra: int = 0
        unlocked_bra: int = 0

        for i, j in zip(s, locked):
            if j == "0":
                unlocked_bra += 1
            else:
                if i == "(":
                    opening_bra += 1
                else:
                    if opening_bra:
                        opening_bra -= 1
                    elif unlocked_bra:
                        unlocked_bra -= 1
                    else:
                        return False

        # check opening brackets
        closing_bra: int = 0
        unlocked_bra: int = 0
        for idx in range(n - 1, -1, -1):
            i, j = s[idx], locked[idx]

            if j == "0":
                unlocked_bra += 1
            else:
                if i == "(":
                    if closing_bra:
                        closing_bra -= 1
                    elif unlocked_bra:
                        unlocked_bra -= 1
                    else:
                        return False
                else:
                    closing_bra += 1
        return True
