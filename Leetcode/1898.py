from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        k,m,n=len(removable),len(s), len(p)

        def is_sub_seq(a:str, b:str)->bool:
            """check if `a` is a sub-seq of `b`"""
            it=iter(b)
            return all(ch in it for ch in a)

        def mask(prefix_len:int):
            nonlocal s, removable
            arr=list(s)
            for i in range(prefix_len):
                arr[removable[i]]=''
            return ''.join(arr)

        lo,hi=0,k
        ans=lo
        while lo<=hi:
            mid=(lo+hi)>>1
            candidate=mask(mid)

            if is_sub_seq(p, candidate):
                lo=mid+1
                ans=mid
            else:
                hi=mid-1
        return ans





def main():
    obj=Solution()

    s="abcacb"
    p="ab"
    arr=[3,1,0]

    s='abcbddddd'
    p='abcd'
    arr=[3,2,1,4,5,6]

    s='abcab'
    p='abc'
    arr=[0,1,2,3,4]

    ans=obj.maximumRemovals(s,p,arr)

    print(ans)

if __name__ == '__main__':
    main()
