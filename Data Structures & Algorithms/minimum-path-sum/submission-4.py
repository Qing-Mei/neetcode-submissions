from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @cache
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return float("inf")
            
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            return min(dfs(i + 1, j), dfs(i, j + 1)) + grid[i][j]
        
        return dfs(0, 0)
