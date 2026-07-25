class Solution:
    def exitPoint(self, mat: list[list[int]]) -> list[int]:
        n, m = len(mat), len(mat[0])

        def is_valid_pos(_x: int, _y: int) -> bool:
            nonlocal n, m
            return 0 <= _x < n and 0 <= _y < m

        dirs: tuple[tuple[int, int], ...] = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        )

        curr_dir_idx = 0
        x, y = 0, -1
        while True:
            nx, ny = x + dirs[curr_dir_idx][0], y + dirs[curr_dir_idx][1]

            if not is_valid_pos(nx, ny):
                return [x, y]

            if mat[nx][ny] == 1:
                curr_dir_idx = (curr_dir_idx + 1) % 4
                mat[nx][ny] = 0

            x, y = nx, ny

        return [-1, -1]
