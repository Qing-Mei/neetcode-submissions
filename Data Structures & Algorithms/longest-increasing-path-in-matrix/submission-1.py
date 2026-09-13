from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        indegree = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for di, dj in dirs:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                        indegree[ni][nj] += 1
        
        q = deque()

        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    q.append((i, j))
        
        best = 0

        while q:
            sz = len(q)

            for _ in range(sz):
                i, j = q.popleft()

                for di, dj in dirs:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                        indegree[ni][nj] -= 1
                        if indegree[ni][nj] == 0:
                            q.append((ni, nj))
            best += 1
        
        return best
