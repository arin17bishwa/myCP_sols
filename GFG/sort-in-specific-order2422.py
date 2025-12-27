class Solution:
    def sortIt(self, arr: list[int]) -> None:
        odds = []
        evens = []
        for i in arr:
            if i & 1:
                odds.append(i)
            else:
                evens.append(i)

        odds.sort(reverse=True)
        evens.sort()
        arr[:] = odds + evens
