from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        closing_mapping = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        st = deque([])
        for ch in s:
            if ch not in closing_mapping:
                st.append(ch)
            elif st and st[-1] == closing_mapping[ch]:
                st.pop()
            else:
                return False

        return not st
