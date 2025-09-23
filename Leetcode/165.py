class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        l1 = list(map(int, version1.split(".")))
        l2 = list(map(int, version2.split(".")))
        if len(l1) < len(l2):
            l1.extend([0] * (len(l2) - len(l1)))
        else:
            l2.extend([0] * (len(l1) - len(l2)))

        print(l1)
        print(l2)

        if l1 < l2:
            return -1
        elif l1 > l2:
            return 1
        return 0


def main():
    obj = Solution()

    v1 = "1.0.1"
    v2 = "1"

    ans = obj.compareVersion(v1, v2)

    print(ans)


if __name__ == "__main__":
    main()
