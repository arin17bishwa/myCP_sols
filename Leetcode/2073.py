from typing import List
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        arr=tickets
        t=arr[k]
        n=len(arr)
        ans=t

        for i in range(n):
            if i<k:
                ans+=1+min(t-1,arr[i]-1)
            elif i>k:
                ans+=min(t-1,arr[i])
        return ans

def main():
    obj=Solution()

    arr=[2,3,2]
    k=2

    # arr=[5,1,1,1]
    # k=0

    # arr=[84,49,5,24,70,77,87,8]
    # k=3

    ans=obj.timeRequiredToBuy(arr,k)

    print(ans)

if __name__ == '__main__':
    main()