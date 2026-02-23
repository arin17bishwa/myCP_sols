class Solution:
    def getLastMoment(self, n:int, left:list[int], right:list[int])->int:
        return max(max(left, default=0), n-min(right, default=n))