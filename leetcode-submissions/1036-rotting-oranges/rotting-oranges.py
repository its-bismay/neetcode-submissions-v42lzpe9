class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def rotting(r, c):
            nonlocal fresh
            if(
                min(r,c) < 0 or
                r >= rows or
                c >= cols or
                (r, c) in visited or
                grid[r][c] != 1
            ):
                return

            visited.add((r,c))
            fresh -= 1
            q.append([r,c])

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
        
        time = 0
        while q and fresh > 0:
            for i  in range(len(q)):
                r, c = q.popleft()

                rotting( r , c + 1)
                rotting( r , c - 1)
                rotting( r - 1 , c)
                rotting( r + 1 , c)
            
            time += 1
        
        return time if fresh == 0 else -1
        