class Solution:
    def maxSubarraySum(self, arr:list[int], k:int)->int:
        n = len(arr)
        curr=0
        for i in range(k):
            curr+=arr[i]
        ans=curr

        for i in range(k,n):
            curr-=arr[i-k]
            curr+=arr[i]
            ans=max(ans,curr)
        return ans
