class Solution:
    def cntWays(self, arr:list[int])->int:
        n=len(arr)
        suffix=arr[:]

        for i in range(n-2,0,-1):
            suffix[i-1]+=suffix[i+1]
        suffix.extend([0,0])

        # print(suffix)
        ans=prefix=prefix_prev=0

        for i in range(n):
            if prefix+suffix[i+2]==prefix_prev+suffix[i+1]:
                ans+=1
            prefix_prev+=arr[i]
            prefix,prefix_prev=prefix_prev,prefix

        return ans


def main():
    obj=Solution()
    arr=[2, 1, 6, 4]
    arr=[1, 1, 1]

    ans=obj.cntWays(arr)

    print(ans)

if __name__ == '__main__':
    main()