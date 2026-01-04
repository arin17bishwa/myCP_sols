from functools import cache
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        arr=nums

        ans=0

        for i in arr:
            sm=self.sum_divisors(i)
            if sm>0:
                ans+=1+i+sm
        return ans

    @staticmethod
    @cache
    def sum_divisors(n:int)->int:
        if n<5:
            return 0
        divisor=-1
        for i in range(2,int(pow(n,0.5))+1):
            if n%i==0:
                if i*i==n:
                    return 0
                if divisor!=-1:
                    return 0
                divisor=i
        return divisor+(n//divisor)


def main():
    obj=Solution()

    arr=[21,4,7]
    arr=[21,21]
    # arr=[1,2,3,4,5]

    ans=obj.sumFourDivisors(arr)
    print(ans)

if __name__ == '__main__':
    main()