from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr=numbers
        n=len(arr)

        lo,hi=0,n-1

        while lo<hi:
            sm=arr[lo]+arr[hi]

            if sm==target:
                return [lo+1,hi+1]

            if sm<target:
                lo+=1
            else:
                hi-=1
        return [-1,-1]