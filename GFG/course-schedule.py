class Solution:
    def findOrder(self, n: int, prerequisites: list[list[int]]):
        g: dict[int, list[int]] = {i: [] for i in range(n)}
        for i, j in prerequisites:
            g[j].append(i)

        vis: set[int] = set()
        st: list[int] = []

        def dfs(u: int):
            nonlocal vis, g, st
            vis.add(u)

            for v in g.get(u, []):
                if v not in vis:
                    dfs(v)

            st.append(u)

        for k in g.keys():
            if k not in vis:
                dfs(k)

        return st[::-1]


def main():
    obj = Solution()
    n = 3
    arr = [
        [1, 0],
        [2, 1],
    ]

    ans = obj.findOrder(n, arr)

    print(ans)


if __name__ == "__main__":
    main()
