class Solution:
    def binaryGap(self, n: int) -> int:
        while n and n&1==0:
            n>>=1
        if n<3:
            return 0
        ans=0
        while n:
            curr=0
            while n and n&1==0:
                n>>=1
                curr+=1
            ans=max(ans,curr+1)
            n>>=1
        return ans
