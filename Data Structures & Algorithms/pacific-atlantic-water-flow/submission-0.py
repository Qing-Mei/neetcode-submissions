class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(i, j, visited):
            visited.add((i, j))

            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, visited)

        
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)
        
        return [[i, j] for i, j in pacific & atlantic]
