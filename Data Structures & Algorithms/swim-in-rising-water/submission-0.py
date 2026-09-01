import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        heap = [(grid[0][0], 0, 0)]
        visited = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m = len(grid)
        n = len(grid[0])

        while heap:
            water, i, j = heapq.heappop(heap)

            if (i, j) in visited:
                continue
            
            visited.add((i, j))
            
            if i == m - 1 and j == n - 1:
                return water
            
            for di, dj in dirs:
                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    new_water = max(water, grid[ni][nj])
                    heapq.heappush(heap, (new_water, ni, nj))
        