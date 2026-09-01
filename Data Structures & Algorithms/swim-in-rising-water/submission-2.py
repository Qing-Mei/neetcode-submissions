from collections import deque

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def can_finish(water):
            if grid[0][0] > water:
                return False
            
            q = deque([(0, 0)])
            visited = {(0, 0)}

            while q:
                x, y = q.popleft()

                if x == n - 1 and y == n - 1:
                    return True
                
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] <= water:
                        q.append((nx, ny))
                        visited.add((nx, ny))

        l = max(grid[0][0], grid[n - 1][n - 1])
        r = n * n - 1

        while l < r:
            m = (l + r) // 2

            if can_finish(m):
                r = m
            else:
                l = m + 1
        
        return l

