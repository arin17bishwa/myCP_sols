from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        arr = sandwiches
        n = len(arr)
        zeros = students.count(0)
        ans = n
        cnt = [zeros, n - zeros]

        for i in sandwiches:
            if cnt[i] < 1:
                break
            ans -= 1
            cnt[i] -= 1
        return ans


def main():
    obj = Solution()

    l1 = [1, 1, 0, 0]
    l2 = [0, 1, 0, 1]

    l1 = [1, 1, 1, 0, 0, 1]
    l2 = [1, 0, 0, 0, 1, 1]

    ans = obj.countStudents(l1, l2)

    print(ans)


if __name__ == "__main__":
    main()
