from typing import List, Union


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        arr: List[Union[int, str]] = words
        n = len(arr)
        vowels = "aeiou"

        for i in range(n):
            if (arr[i][0] in vowels) and (arr[i][-1] in vowels):
                arr[i] = 1
            else:
                arr[i] = 0
            if i:
                arr[i] += arr[i - 1]

        q = len(queries)
        ans = [0] * q

        for i in range(q):
            start, end = queries[i]
            ans[i] = arr[end] - (0 if start == 0 else arr[start - 1])
        return ans
