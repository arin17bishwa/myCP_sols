from collections import deque


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A: str) -> int:
        st = deque()
        s = A
        for i in s:
            if i == ")" and st and st[-1] == "(":
                st.pop()
            else:
                st.append(i)
        return 0 if st else 1
