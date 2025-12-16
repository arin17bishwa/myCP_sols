from typing import List


class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        self.tree: list[None | int] = [None] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _build(self, idx, l, r):
        if l == r:
            ch = self.s[l]
            self.tree[idx] = (ch, ch, 1)
            return

        mid = (l + r) // 2
        self._build(idx * 2, l, mid)
        self._build(idx * 2 + 1, mid + 1, r)

        self.tree[idx] = self._merge(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def _merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        left_char = a[0]
        right_char = b[1]
        runs = a[2] + b[2]
        if a[1] == b[0]:
            runs -= 1
        return left_char, right_char, runs

    def update(self, pos):
        self.s[pos] = "A" if self.s[pos] == "B" else "B"
        self._update(1, 0, self.n - 1, pos)

    def _update(self, idx, l, r, pos):
        if l == r:
            ch = self.s[l]
            self.tree[idx] = (ch, ch, 1)
            return
        mid = (l + r) // 2
        if pos <= mid:
            self._update(idx * 2, l, mid, pos)
        else:
            self._update(idx * 2 + 1, mid + 1, r, pos)

        self.tree[idx] = self._merge(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def query(self, ql, qr):
        return self._query(1, 0, self.n - 1, ql, qr)

    def _query(self, idx, l, r, ql, qr):
        if qr < l or r < ql:
            return None
        if ql <= l and r <= qr:
            return self.tree[idx]
        mid = (l + r) // 2
        left = self._query(idx * 2, l, mid, ql, qr)
        right = self._query(idx * 2 + 1, mid + 1, r, ql, qr)
        return self._merge(left, right)


class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        st = SegmentTree(s)
        ans: list[int] = []
        n = len(s)
        for q in queries:
            if len(q) == 2:
                st.update(q[1])
            else:
                _, left, right = q
                node = st.query(left, right)
                ans.append(right - left + 1 - node[2])
        return ans
