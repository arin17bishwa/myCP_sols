from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends)
        ans = []
        for i in order:
            if i in friends:
                ans.append(i)
        return ans
