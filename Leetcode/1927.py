class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left_q = right_q = 0
        left_sm = right_sm = 0
        for i in range(n // 2):
            if num[i] == "?":
                left_q += 1
            else:
                left_sm += int(num[i])

        for i in range(n // 2, n):
            if num[i] == "?":
                right_q += 1
            else:
                right_sm += int(num[i])

        if left_q + right_q == 0:
            return left_sm != right_sm

        if (left_q + right_q) & 1:
            return True
        else:
            if left_q == right_q:
                return left_sm != right_sm
            else:
                return 9 * (left_q - right_q) != 2 * (right_sm - left_sm)
