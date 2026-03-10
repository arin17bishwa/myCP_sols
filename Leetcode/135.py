from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr=ratings
        n=len(arr)

        ans=[1]*n

        for i in range(1,n):
            if arr[i]>arr[i-1]:
                ans[i]=ans[i-1]+1

        for i in range(n-2,-1,-1):
            if arr[i]>arr[i+1]:
                ans[i]=max(ans[i], ans[i+1]+1)

        return sum(ans)

def main():
    obj=Solution()

    arr=[1,0,2]
    arr=[1,2,2]
    arr=[1,3,2,2,1]
    arr=[1,2,87,87,87,2,1]

    ans=obj.candy(arr)

    print(ans)

if __name__ == '__main__':
    main()