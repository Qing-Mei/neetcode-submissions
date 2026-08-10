class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        def dfs(i, j):
            grid[i][j] = "0"

            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                    dfs(ni, nj)
        
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        
        return cnt
        