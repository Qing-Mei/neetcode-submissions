from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
            
        q = deque()

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        steps = 0
        INF = 2 ** 31 - 1
        while q:
            sz = len(q)

            for _ in range(sz):
                x, y = q.popleft()

                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == INF:
                        grid[nx][ny] = grid[x][y] + 1
                        q.append((nx, ny))
            
            steps += 1
