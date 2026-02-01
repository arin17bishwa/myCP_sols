from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        arr = students
        n = len(arr)
        ones = arr.count(1)
        zeros = n - ones
        ans = n
        for sandwich in sandwiches:
            if sandwich == 1:
                if ones > 0:
                    ones -= 1
                else:
                    return ans
            else:
                if zeros > 0:
                    zeros -= 1
                else:
                    return ans
            ans -= 1
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
