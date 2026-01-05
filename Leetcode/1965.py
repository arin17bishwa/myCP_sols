from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg=abs_sm=0
        mn=(10**9)
        has_zero=False

        for row in matrix:
            for ele in row:
                if ele==0:
                    has_zero=True
                else:
                    if ele<0:
                        neg+=1
                    mn=min(mn,abs(ele))

                abs_sm+=abs(ele)

        if has_zero or  neg&1==0:
            return abs_sm
        else:
            return abs_sm-2*mn

def main():

    obj=Solution()

    arr=[[1,-1],[-1,1]]
    arr=[[1,2,3],[-1,-2,-3],[1,2,3]]
    arr=[[-1,0,-1],[-2,1,3],[3,2,2]]
    arr=[[2,9,3],[5,4,-4],[1,7,1]]

    ans=obj.maxMatrixSum(arr)
    print(ans)

if __name__ == '__main__':
    main()