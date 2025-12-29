class Solution:
    def kthElement(self, a: list[int], b: list[int], k: int) -> int:
        i = j = 0
        flag = 0
        m, n = len(a), len(b)
        for _ in range(k):
            if i < m and j < n:
                if a[i] < b[j]:
                    i += 1
                    flag = 0
                else:
                    j += 1
                    flag = 1
            elif i < m:
                flag = 0
                i += 1
            else:
                flag = 1
                j += 1
        return a[i - 1] if flag == 0 else b[j - 1]


def main():
    obj = Solution()
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 1

    ans = obj.kthElement(a, b, k)

    # print(ans)


if __name__ == "__main__":
    main()
