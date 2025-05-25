class Solution:
    def pythagoreanTriplet(self, arr: list[int]):
        arr.sort()
        n = len(arr)
        elements = set(arr)

        for i, a in enumerate(arr):
            for j in range(i + 1, n):
                b = arr[j]
                x2 = a * a + b * b
                if not self.is_perfect_square(x2):
                    continue
                if int(pow(x2, 0.5)) in elements:
                    return True
        return False

    @staticmethod
    def is_perfect_square(n: int):
        t = pow(n, 0.5)
        return t % 1 == 0 and t * t == n
