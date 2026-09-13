from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @cache
        def dfs(i, j):
            best = 1
            
            for di, dj in dirs:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1 + dfs(ni, nj))
        
            return best

        res = 1
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        
        return res
