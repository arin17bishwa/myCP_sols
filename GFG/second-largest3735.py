class Solution:
    def getSecondLargest(self, arr: list[int]) -> int:
        arr=sorted(set(arr))
        if len(arr)<2:
            return -1
        return arr[-2]

def main():
    obj = Solution()

    arr = [10, 5, 10]
    arr=[10,10,1]

    ans = obj.getSecondLargest(arr)

    # print(ans)


if __name__ == "__main__":
    main()
