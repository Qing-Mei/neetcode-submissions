import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        min_heap = []

        m = len(heights)
        n = len(heights[0])

        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0

        heapq.heappush(min_heap, (0, 0, 0)) # effort, x, y

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            effort, x, y = heapq.heappop(min_heap)

            if effort > dist[x][y]:
                continue
            
            if x == m - 1 and y == n - 1:
                return effort
            
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    edge_effort = abs(heights[nx][ny] - heights[x][y])
                    new_effort = max(edge_effort, effort)

                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heapq.heappush(min_heap, (new_effort, nx, ny))
        