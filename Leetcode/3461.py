class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = list(map(int, s))
        while len(arr) > 2:
            temp = [(arr[i - 1] + arr[i]) % 10 for i in range(1, len(arr))]
            arr[:] = temp[:]
        return arr[-1] == arr[0]
