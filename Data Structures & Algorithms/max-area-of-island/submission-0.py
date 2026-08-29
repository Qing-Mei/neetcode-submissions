class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j, area):
            grid[i][j] = 0
            area = 1

            for di, dj in dirs:
                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    area += dfs(ni, nj, area)
            
            return area
        
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j, 0))
        
        return max_area
