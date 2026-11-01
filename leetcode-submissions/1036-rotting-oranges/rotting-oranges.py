class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()
        visited = [[0] * m for _ in range(n)]
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append(([i, j], 0))
                    visited[i][j] = 2
                if grid[i][j] == 1:
                    fresh += 1

        mt = 0
        while q:
            loc, t = q.popleft()
            mt = max(mt, t)
            r, c = loc
            directions = [
                (-1, 0), # top
                (1, 0), # buttom
                (0, -1), # left
                (0, 1)  # right
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr >= 0 and nr < n and nc >= 0 and nc < m and visited[nr][nc] == 0 and grid[nr][nc] == 1):
                    fresh -= 1
                    q.append(([nr, nc], t + 1))
                    visited[nr][nc] = 2
            
        return -1 if fresh > 0 else mt

        