from typing import List

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        arr=instructions
        n=len(arr)
        ans=idx=0

        while 0<=idx<n and arr[idx]!='':
            ins=arr[idx]
            arr[idx]=''
            if ins=='add':
                ans+=values[idx]
                idx+=1
            else:
                idx=idx+values[idx]

        return ans
