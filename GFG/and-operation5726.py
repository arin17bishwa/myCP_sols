class Solution:
    def andInRange(self, l: int, r: int):
        shift=0

        while l!=r:
            l>>=1
            r>>=1
            shift+=1
        return l<<shift


def main():
    obj = Solution()

    l, r = 8, 13
    # l, r = 2, 3
    # l,r=4,5

    ans = obj.andInRange(l, r)

    # print(ans)


if __name__ == "__main__":
    main()
