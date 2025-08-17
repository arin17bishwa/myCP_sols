class Solution:
    def maximum69Number(self, num: int) -> int:
        for i in range(5, -1, -1):
            if (num // pow(10, i)) % 10 == 6:
                num += 3 * (pow(10, i))
                break
        return num
