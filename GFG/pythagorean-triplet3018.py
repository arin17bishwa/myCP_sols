class Solution:
    def pythagoreanTriplet(self, arr: list[int]):
        arr.sort()
        n = len(arr)
        squares = set(map(lambda x: x * x, arr))
        mx = max(arr)
        for i in range(1, mx + 1):
            for j in range(i + 1, mx + 1):
                if all(map(lambda x: x in squares, (i * i, j * j, i * i + j * j))):
                    return True
        return False
