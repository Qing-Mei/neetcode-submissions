from functools import cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @cache
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or obstacleGrid[i][j] == 1:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)
