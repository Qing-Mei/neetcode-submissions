class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total = n * n

        positions = [None] * total
        for i in range(n):
            for j in range(n):
                positions[grid[i][j]] = (i, j)

        active = [False] * total

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        parent = list(range(total))
        size = [1] * total

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return
            
            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x
            
            parent[root_y] = root_x
            size[root_x] += size[root_y]

        for water in range(total):
            x, y = positions[water]
            idx = x * n + y
            active[idx] = True

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    nei = nx * n + ny

                    if active[nei]:
                        union(idx, nei)
            
            if active[0] and active[total - 1]:
                if find(0) == find(total - 1):
                    return water
