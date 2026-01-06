class Solution:
    def maxSubarrayXOR(self, arr:list[int], k:int)->int:
        curr=0
        n=len(arr)
        for i in range(k):
            curr^=arr[i]
        ans=curr

        for i in range(k,n):
            curr^=arr[i]^arr[i-k]
            ans=max(ans, curr)
        return ans
