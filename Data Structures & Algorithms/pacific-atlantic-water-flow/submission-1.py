class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, visited):
            visited.add((x, y))

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and heights[nx][ny] >= heights[x][y]:
                    dfs(nx, ny, visited)


        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)
        
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        
        return [[i, j] for i, j in pacific & atlantic]
