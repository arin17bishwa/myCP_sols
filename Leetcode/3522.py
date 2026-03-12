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

def main():
    obj=Solution()

    ins=["jump","add","add","jump","add","jump"]
    val=[2,1,3,1,-2,-3]

    ins=["jump","add","add"]
    val=[3,1,1]

    ins=['jump']
    val=[0]

    ans=obj.calculateScore(ins,val)

    print(ans)

if __name__ == '__main__':
    main()

