# region fastio
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion


def intArr():
    return map(int, input().split())


def In():
    return int(input())


def func():
    pass


def main():
    for _ in range(In()):
        print(func())
    return


if __name__ == "__main__":
    main()


# region YES/NO Decorator


def yn_dec(function, letter_case="upper"):
    def inner1(*args, **kwargs):
        res = function(*args, **kwargs)
        if letter_case == "upper":
            return "YES" if res else "NO"
        if letter_case == "title":
            return "Yes" if res else "No"
        if letter_case == "lower":
            return "yes" if res else "no"
        if res:
            return "YES"
        return "NO"

    return inner1


# endregion

# region smaller_fastio
from sys import stdin, stdout


def I():
    return int(stdin.readline())


def In():
    return map(int, stdin.readline().split())


def S():
    return stdin.readline().rstrip()


def Sn():
    return stdin.readline().split(" ")


def Out(whatever):
    return stdout.write(whatever)


# endregion

# region bisection methods
from bisect import bisect_right, bisect_left


def index(a, x):
    "Locate the leftmost value exactly equal to x"
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):
    "Find rightmost value less than x"
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_le(a, x):
    "Find rightmost value less than or equal to x"
    i = bisect_right(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):
    "Find leftmost value greater than x"
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_ge(a, x):
    "Find leftmost item greater than or equal to x"
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


# endregion

# region segment-tree(personal)
"""
        Implementation wrt summation
"""
global tree, arr


def eff_build(arr):
    n = len(arr)
    seg = [0] * ((n << 1) + 1)
    for i in range(n):
        seg[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        seg[i] = seg[i << 1] + seg[i << 1 | 1]
    # print(seg)
    return seg


def build(arr):
    n = len(arr)
    seg = [0] * (4 * n + 1)
    _build(arr, seg, 0, 0, n - 1)
    return seg


def _build(arr, seg, ind, l, r):  # zero indexed
    if l == r:
        seg[ind] = arr[l]
        return seg[ind]

    mid = (l + r) // 2
    left = _build(arr, seg, (ind << 1) + 1, l, mid)
    right = _build(arr, seg, (ind << 1) + 2, mid + 1, r)
    seg[ind] = left + right
    return seg[ind]


def query(seg, ind, l, r, L, R):
    if r < L or l > R:
        return 0
    if l >= L and r <= R:
        return seg[ind]
    mid = (l + r) // 2
    left = query(seg, (ind << 1 | 1), l, mid, L, R)
    right = query(
        seg,
        (ind << 1) + 2,
        mid + 1,
        r,
        L,
        R,
    )
    return left + right  # Sum


def point_update(seg, node, l, r, ind, val):
    # print(node, l, r)
    if ind < l or ind > r:
        return
    if r <= ind <= l:
        seg[node] = val
        return
    mid = (l + r) >> 1
    point_update(seg, (node << 1 | 1), l, mid, ind, val)
    point_update(seg, (node << 1) + 2, mid + 1, r, ind, val)
    seg[node] = seg[(node << 1 | 1)] + seg[(node << 1) + 2]  # Sum


# endregion

# region persistent segment tree
BIG = 10**9

vals = []
L = []
R = []


def create(n):
    """create a persistent segment tree of size n"""

    ind = len(vals)
    vals.append(BIG)

    L.append(-1)
    R.append(-1)

    if n == 1:
        L[ind] = -1
        R[ind] = -1
    else:
        mid = n // 2
        L[ind] = create(mid)
        R[ind] = create(n - mid)
    return ind


def setter(ind, i, val, n):
    """set set[i] = val for segment tree ind, of size n"""

    ind2 = len(vals)
    vals.append(BIG)

    L.append(-1)
    R.append(-1)

    if n == 1:
        vals[ind2] = val
        return ind2

    mid = n // 2
    if i < mid:
        L[ind2] = setter(L[ind], i, val, mid)
        R[ind2] = R[ind]
    else:
        L[ind2] = L[ind]
        R[ind2] = setter(R[ind], i - mid, val, n - mid)
    vals[ind2] = min(vals[L[ind2]], vals[R[ind2]])
    return ind2


def minimum(ind, l, r, n):
    """find mimimum of set[l:r] for segment tree ind, of size n"""

    if l == 0 and r == n:
        return vals[ind]
    mid = n // 2
    if r <= mid:
        return minimum(L[ind], l, r, mid)
    elif mid <= l:
        return minimum(R[ind], l - mid, r - mid, n - mid)
    else:
        return min(minimum(L[ind], l, mid, mid), minimum(R[ind], 0, r - mid, n - mid))


# endregion


# region DisjointSetUnion
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)


# endregion


# region sieve of Eratosthenes
def prime_sieve(n):
    """returns a sieve of primes >= 5 and < n"""
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    """returns a list of primes <= n"""
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend(
            3 * i + 1 | 1
            for i in range(1, (n + 1) // 3 + (n % 6 == 1))
            if not (sieve[i >> 3] >> (i & 7)) & 1
        )
    return res


# endregion

# region combinatorics nos

import math
import operator as op
from functools import reduce


def memoize(f):
    """memoization decorator for a function taking one or more arguments"""

    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret

    return memodict().__getitem__


@memoize
def catalan_recursive(n):
    if n == 0:
        return 1
    return (2 * (2 * n - 1) * catalan_recursive(n - 1)) // (n + 1)


@memoize
def euler_recursive(n, k):
    if (k == 0) or (n - 1 == k):
        return 1
    return (n - k) * euler_recursive(n - 1, k - 1) + (k + 1) * euler_recursive(n - 1, k)


@memoize
def stirling_1_recursive(n, k):
    if n == k == 0:
        return 1
    if (n == 0) or (k == 0):
        return 0
    return stirling_1_recursive(n - 1, k - 1) + (n - 1) * stirling_1_recursive(n - 1, k)


@memoize
def stirling_2_recursive(n, k):
    if (k == 1) or (n == k):
        return 1
    return stirling_2_recursive(n - 1, k - 1) + k * stirling_2_recursive(n - 1, k)


nCr = lambda n, r: reduce(op.mul, range(n - r + 1, n + 1), 1) // math.factorial(r)

multinomial = lambda k: math.factorial(sum(k)) // reduce(
    op.mul, (math.factorial(i) for i in k)
)

derangements = lambda n: int(math.factorial(n) / math.e + 0.5)

bell = lambda n: sum(stirling_2_recursive(k, n) for k in range(n + 1))

catalan = lambda n: nCr(2 * n, n) // (n + 1)

euler = lambda n, k: sum(
    (1 - 2 * (j & 1)) * nCr(n + 1, j) * ((k + 1 - j) ** n) for j in range(k + 1)
)

stirling_2 = lambda n, k: sum(
    ((-1) ** (k - j)) * nCr(k, j) * (j**n) for j in range(k + 1)
) // math.factorial(k)

# endregion

# region segmented sieve(for PRIMES)


def func(left, right):
    PRIMES = []
    arr = [True] * (right - left + 1)
    for i in PRIMES:
        for j in range(max(i * i, (left + i - 1) // i * i), right + 1, i):
            arr[j - left] = False
    if left == 1:
        arr[0] = False
    for i in range(right - left + 1):
        if arr[i]:
            print(left + i)
    return


# endregion

# region Lazy segment Tree


class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size : _size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = (
                self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            )
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)


# endregion


# region Stack
from collections import deque


class Stack(deque):
    def empty(self):
        return len(self) == 0

    def top(self):
        x = self.pop()
        self.append(x)
        return x

    def bottom(self):
        x = self.popleft()
        self.appendleft(x)
        return x


# endregion


# region SortedList
class SortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i : i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False

    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1

        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi

        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True

    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError("{0!r} not in list".format(value))

    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)

    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        """Return string representation of sorted list."""
        return "SortedList({0})".format(list(self))


# endregion


if __name__ == "__main__":
    arr = [i for i in range(1000000)]
    tree = build(arr)
    print(query(tree, 0, 0, len(arr) - 1, 0, 13000))
    point_update(tree, 0, 0, len(arr) - 1, 0, 15)
    print(query(tree, 0, 0, len(arr) - 1, 0, 130))
    pass
