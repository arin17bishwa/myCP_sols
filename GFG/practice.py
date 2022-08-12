import heapq
from typing import *

import sys
import time

sys.stdin = open('/home/bishwajit/HDD/PycharmPro/myCP_sols/in.txt', 'r')


# # region fastio
# import os
# import sys
# from io import BytesIO, IOBase
# 
# BUFSIZE = 8192
# 
# 
# class FastIO(IOBase):
#     newlines = 0
# 
#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None
# 
#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()
# 
#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()
# 
#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)
# 
# 
# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")
# 
# 
# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")
# 
# 
# # endregion


def intArr(sep=' '):
    return map(int, input().split(sep))


def In():
    return int(input())


def twoDParser(list_sep='],[', element_sep=',', string=False) -> List[List[int]]:
    """
    for input of formats
    [[2,3,4,2],[3,4],[6,5,7],[4,1,8,3]]
    """
    s = input()
    s = s[2:-2]
    l1 = []
    for i in s.split(list_sep):
        l1.append(list(map(int if not string else str, i.split(element_sep))))
    return l1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}->{self.next}"


def listifyListNode(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans


# from collections import defaultdict
#
#
# class TrieNode:
#     def __init__(self):
#         self.nodes = defaultdict(TrieNode)
#         self.word_end = False
#
#     def has_node(self, key: str):
#         return self.nodes.get(key) is not None
#
#     def get_next_node(self, key: str):
#         return self.nodes[key]
#
#     def end_word(self):
#         self.word_end = True
#
#     def is_word(self):
#         return self.word_end
#
#     def __str__(self):
#         return f"{self.nodes.keys()}"

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def completeRows(self, n: int) -> int:
        # code here
        lo, hi = 1, 10 ** 8
        ans = 1
        while lo <= hi:
            # print(lo, hi)
            mid = (lo + hi) // 2
            x = (mid * (mid + 1)) // 2
            if x <= n:
                lo = mid + 1
                ans = mid
            else:
                hi = mid - 1
                # ans = hi
        return ans


def funct(a):
    s = Solution()
    return s.completeRows(a)


def fun1(tempChange):
    arr = tempChange
    n = len(arr)
    pre = arr[:]
    for i in range(1, n):
        pre[i] += pre[i - 1]
    ans = -float('inf')
    for i in range(n):
        if i == 0:
            ls = pre[0]
            rs = pre[-1]
        else:
            ls = pre[i]
            rs = pre[-1] - pre[i - 1]
        ans = max(ans, max(ls, rs))
    return ans


def main():
    _t1 = time.perf_counter()
    while 1:
        try:
            a = In()
            # a, b = intArr()
            print(funct(a))
            print('-' * 60)
        except EOFError as e:
            break
    print(time.perf_counter() - _t1)


if __name__ == '__main__':
    main()
