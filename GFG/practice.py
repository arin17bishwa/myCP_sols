import heapq
from typing import *

import sys
import time


# sys.stdin = open('/media/bishwajit/HDD/PycharmPro/myCP_sols/in.txt', 'r')


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


from itertools import groupby
from collections import defaultdict


def func(s: str, k: int):
    l1 = [(i, len(list(j))) for i, j in groupby(s)]
    n = len(l1)
    curr = ans = j = cnt = 0
    freq = [0] * 26
    for i in range(n):
        while j <= i and cnt > k:
            curr -= l1[j][1]
            _ch = ord(l1[j][0]) - 97
            freq[_ch] -= l1[j][1]
            if freq[_ch] == 0:
                cnt -= 1
            j += 1
        if cnt == k:
            ans = max(curr, ans)
        ch_ord = ord(l1[j][0]) - 97
        if freq[ch_ord] == 0:
            cnt += 1
        freq[ch_ord] += l1[i][1]
    return ans


from collections import defaultdict


class Trie:

    def __init__(self):
        self.d = defaultdict(Trie)
        self.count = 0

    def insert(self, word: str):
        curr = self
        for ch in word:
            curr = curr.d[ch]
            curr.count += 1

    def get_count(self, word: str) -> int:
        ans = 0
        curr = self
        for ch in word:
            curr = curr.d[ch]
            if curr.count == 0:
                return 0
        return curr.count


def nearest_smaller(arr: list):
    n = len(arr)
    s = []
    ans = []
    for i in range(n):
        x = arr[i]
        while s and s[-1] >= arr[i]:
            s.pop()
        if not s:
            ans.append(-1)
        else:
            ans.append(s[-1])
        s.append(arr[i])
    return ans


def driver_code_1():
    _ = input()
    arr = list(map(int, input().split()))
    print(*nearest_smaller(arr))


def min_sum_subarray(arr: list, k: int):
    n = len(arr)
    s = sum(arr)
    k = n - k
    ans = curr = sum(arr[1:k + 1])
    prev = arr[0]
    for i in range(k + 1, n):
        x = arr[i - k]
        curr -= x
        prev += x
        curr += arr[i]
        ans = min(curr, ans)
    return ans


def driver_code_2():
    n, k = (map(int, input().split()))
    arr = list(map(int, input().split()))
    print(sum(arr) - min_sum_subarray(arr, k))


def main():
    _t1 = time.perf_counter()
    while 1:
        try:
            # a = In()
            # a, b = intArr()
            s = input()
            k = In()
            print(func(s, k))
            print('-' * 60)
        except EOFError as e:
            break
    print(time.perf_counter() - _t1)


from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10 ** 5 + 5)


def getVisibleProfilesCount(connection_nodes: int, connection_from: list, connection_to: list, queries: list):
    g = defaultdict(list)
    for i, j in zip(connection_from, connection_to):
        g[i].append(j)
        g[j].append(i)
    for i in range(1, connection_nodes + 1):
        g[i].append(i)
    curr = 0
    vis = set()
    ans = defaultdict(lambda: 1)

    def dfs(u: int):
        nonlocal curr, vis, _vis, g
        vis.add(u)
        _vis.add(u)
        curr += 1
        for v in g[u]:
            if (u != v) and (v not in vis):
                dfs(v)

    for i in range(1, connection_nodes + 1):
        if i in vis:
            continue
        _vis = set()
        curr = 0
        dfs(i)
        for j in _vis:
            ans[j] = curr

    return [ans[i] for i in queries]


def getEarliestMeetTime(events: list, k: int):
    arr = events
    n = len(arr)
    l1 = [0] * (24 * 60 + 1)
    m = len(l1)

    def parse_time(s: str):
        return tuple(map(int, s.split(':')))

    def parse_min(t: int):
        return '{:02d}:{:02d}'.format(t // 60, t % 60)

    for i in arr:
        _, _, st, e = i.split()
        a, b = parse_time(st)
        c, d = parse_time(e)
        l1[a * 60 + b] += 1
        l1[c * 60 + d + 1] -= 1
    for i in range(1, m):
        l1[i] += l1[i - 1]
    curr = 0
    for i in range(k):
        curr += l1[i]

    if curr == 0:
        return '00:00'

    for i in range(k, m - 1):
        curr += l1[i]
        curr -= l1[i - k]
        if curr == 0:
            return parse_min(i - k + 1)
    return '-1'


def orderConfirmation(orderID: int) -> int:
    ans = 1
    for i in str(orderID):
        ans *= int(i)
    return ans


def noOfProducts(order: list, disAmount: int) -> int:
    return sum(disAmount % i == 0 for i in order)


def func(arr: list):
    n = len(arr)
    ans = []
    curr = []

    def backtrack(idx: int):
        if idx == n:
            ans.append(''.join(curr))
            return
        for ch in arr[idx]:
            curr.append(ch)
            backtrack(idx + 1)
            curr.pop()

    backtrack(0)
    print(ans)


def main():
    n = 7
    e = 4
    l1 = [1, 2, 3, 5]
    l2 = [2, 3, 4, 6]
    q = [1, 3, 5, 7]
    n = 5
    e = 4
    l1 = [2, 2, 1, 1, ]
    l2 = [1, 3, 3, 4]
    q = [4, 2, 5]
    n = 2
    l1 = [
        'a b 12:00 23:59',
        'c d 00:00 13:00'
    ]
    k = 1
    l1 = [
        'a b 12:00 18:59',
        'a b 00:00 11:00'
    ]
    k = 60
    # print(getVisibleProfilesCount(n, l1, l2, q))
    # print(getEarliestMeetTime(l1, k))
    l1 = [
        'ab',
        'xy',
        'mn'
    ]
    func(arr=l1)


if __name__ == '__main__':
    main()
